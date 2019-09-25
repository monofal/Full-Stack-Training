"""
Main Module
"""

from web_scrapper.db.db_helper import DbHelper
from web_scrapper.model.job import Job
from web_scrapper.scrapper.scrapper import Scrapper
from web_scrapper.utils.log_handler import LogHandler
from web_scrapper.utils.utility import Utility

SCRAP_DELAY_TIME = 15


def insert_jobs(new_jobs,
                db_helper):
    """
    Insert job into database
    :param new_jobs: new job
    :param db_helper: db helper
    """
    for job in new_jobs:
        params = Utility.get_param(job)
        query = 'INSERT INTO jobs (company_name, position, location , unique_id)' \
                ' VALUES (%s, %s, %s, %s);'

        db_helper.insert_job(query, params)


def main():
    """
    App entry point
    """
    # Initialization
    db_helper = DbHelper()
    LogHandler.is_log_enabled = Utility.get_log_config()
    log_handler = LogHandler()
    if LogHandler.is_log_enabled:
        log_handler.create_log_file()

    website_url = 'https://news.ycombinator.com/jobs'

    LogHandler.log('info', 'Scrapping started')

    # start scrapping website
    scrapper = Scrapper(website_url)
    new_jobs = scrapper.scrap_website()

    insert_jobs(new_jobs, db_helper)

    LogHandler.log('info', 'Scrapping finished')


if __name__ == "__main__":
    main()
