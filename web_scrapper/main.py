"""
Main Module
"""
import logging

from web_scrapper.db.db_helper import DbHelper
from web_scrapper.model.job import Job
from web_scrapper.scrapper.Scrapper import Scrapper
from web_scrapper.utils.log_handler import LogHandler
from web_scrapper.utils.utility import Utility


def insert_jobs(new_jobs,
                db_helper):
    """
    Bulk insert list of jobs into database
    :param new_jobs: new jobs
    :param db_helper: db helper
    """
    params = Utility.get_params(new_jobs)
    query = 'INSERT INTO Jobs (company_name, location, position, unique_id)' \
            ' VALUES (%s, %s, %s, %s);'

    db_helper.bulk_insertion(query, params)


def get_recently_added_jobs(db_helper):
    """
    Get list of jobs added the last time application ran
    :return: Job , list of recently added jobs
    """
    recent_jobs = []

    query = 'SELECT id,company_name,position,location, unique_id, entry_timestamp FROM Jobs' \
            ' WHERE entry_timestamp IN (SELECT max(entry_timestamp)' \
            ' FROM Jobs)'
    records = db_helper.execute_query(query)

    for row in records:
        recent_jobs.append(fill_job_object(row))

    return recent_jobs


def get_new_records(jobs, recent_jobs):
    """
    Filter out fresh records that are not currently part of our record
    :param jobs: list of jobs extracted from hacker news
    :param recent_jobs: jobs recently added into the database
    :return: Job list , list of fresh records from website
    """
    fresh_records = []
    for job in jobs:
        if not any(job.unique_id == obj.unique_id for obj in recent_jobs):
            fresh_records.append(job)

    return fresh_records


def fill_job_object(row):
    """
    Fill job object
    :param row: single row from database
    :return: Job, job object
    """
    # company_name , position , location , unique_id
    return Job(row[1], row[2], row[3], row[4])


def main():
    """
    App entry point
    """
    # Initialization
    db_helper = DbHelper()
    LogHandler.is_log_enabled = Utility.get_log_config()
    log_handler = LogHandler()
    website_url = 'https://news.ycombinator.com/jobs'

    # Get all jobs added last time the application executed
    recent_jobs = get_recently_added_jobs(db_helper)

    if LogHandler.is_log_enabled:
        logging.info("Scrapping started")

    # start scrapping website
    scrapper = Scrapper(website_url)
    jobs = scrapper.scrap_website()

    # jobs = []
    # jobs.append(Job('asdf', 'asdf', 'asdf', 'asdf_asdf_asdf'))
    # jobs.append(Job('1', '2', '3', '1_2_3'))

    # get list of jobs that aren't part of our record
    new_jobs = get_new_records(jobs, recent_jobs)

    insert_jobs(new_jobs, db_helper)

    # close log file
    log_handler.close_log_file()

    if LogHandler.is_log_enabled:
        logging.info("Scrapping finished")


if __name__ == "__main__":
    main()
