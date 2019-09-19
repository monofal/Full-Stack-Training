"""
Main Module
"""
import json

from web_scrapper.db.db_helper import DbHelper
from web_scrapper.model.job import Job
from web_scrapper.scrapper.Scrapper import Scrapper
from web_scrapper.utils.utility import Utility


def show_jobs(jobs):
    for job in jobs:
        print('company name : {}'.format(job.company_name))
        print('Position : {}'.format(job.position()))
        print('Location : {}'.format(job.location))


def insert_jobs(jobs):
    params = Utility.get_params(jobs)

    db_helper = DbHelper()
    sql = 'INSERT INTO Jobs (company_name, location, position) VALUES (%s, %s, %s);'

    db_helper.bulk_insertion(sql, params)


def main():
    """
    App entry point
    """
    website_url = 'https://news.ycombinator.com/jobs'
    scrapper = Scrapper(website_url)
    jobs = scrapper.scrap_website()

    show_jobs(jobs)

    insert_jobs()




if __name__ == "__main__":
    main()
