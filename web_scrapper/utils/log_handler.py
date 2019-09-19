"""
Log handler
"""
import json
import sys
import time


class LogHandler(object):
    """
    Handle application logging
    """
    is_log_enabled = False

    def __init__(self):
        self.is_log_enabled = self.check_log_enabled()

        time_stamp = time.strftime("%Y%m%d-%H%M%S")

        try:
            # create a new log file
            log_file = open('log_' + time_stamp, "w")
        except:
            print('Error occurred')
            sys.exit(0)

    @staticmethod
    def check_log_enabled():
        try:
            with open('config.json') as config:
                mysql_config = json.load(config)
                return bool(mysql_config["is_log_enables"])
        except FileNotFoundError:
            print('Error')
