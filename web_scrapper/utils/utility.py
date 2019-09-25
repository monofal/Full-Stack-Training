"""
Utility module
"""
import json
import os
import sys

from web_scrapper.utils.log_handler import LogHandler


class Utility(object):
    """
    Class containing utility functions
    """

    @staticmethod
    def get_params(jobs):
        """
        Convert list of job objects into query params
        :param jobs: list of jobs
        :return:
        """
        params = []
        for job in jobs:
            params.append(
                job.company_name,
                job.position,
                job.location,
                # remove all spaces and store unique id in lower case
                '{}_{}_{}'.format(job.company_name, job.position, job.location)
                    .replace(' ', '')
                    .lower())
        return params

    @staticmethod
    def get_param(job):
        """
        Convert job object into tupple
        :param job: list of jobs
        :return: tuple
        """
        return (job.company_name,
                job.position,
                job.location,
                '{}_{}_{}'.format(job.company_name, job.position, job.location)
                .replace(' ', '')
                .lower())

    @staticmethod
    def get_log_config(config_file_path):
        """
        Get configuration for application logging
        """
        try:
            with open(config_file_path) as config:
                mysql_config = json.load(config)
                return mysql_config["log"]["is_log_enabled"] == "True"
        except FileNotFoundError:
            print('Error')
            sys.exit(0)

    @staticmethod
    def get_db_credentials(config_file_path):
        """
        Get database credentials from file
        :return:
        """
        try:
            with open(config_file_path) as config:
                mysql_config = json.load(config)
        except FileNotFoundError:
            LogHandler.log('exception', 'Database configuration file not found')
            raise Exception("Database configuration file not found")

        return mysql_config["mysql"]
