"""
Utility module
"""
import json
import logging
import sys


class Utility(object):
    """
    Class containing utility functions
    """
    @staticmethod
    def get_params(jobs):
        params = []
        for job in jobs:
            params.append((
                job.company_name,
                job.position,
                job.location,
                '{}_{}_{}'.format(job.company_name, job.position, job.location)
            ))
        return params

    @staticmethod
    def get_log_config():
        """
        Get configuration for application logging
        """
        try:
            with open('config.json') as config:
                mysql_config = json.load(config)
                return mysql_config["log"]["is_log_enabled"] == "True"
        except FileNotFoundError:
            print('Error')
            sys.exit(0)

    @staticmethod
    def get_db_credentials():
        """
        Get database credentials from file
        :return:
        """
        try:
            with open('config.json') as config:
                mysql_config = json.load(config)
        except FileNotFoundError:
            logging.exception("Database configuration file not found")

        return mysql_config["mysql"]
