"""
Log handler
"""
import logging
import os
import time


class LogHandler(object):
    """
    Handle application logging
    """
    is_log_enabled = None

    @property
    def is_enabled(self):
        """
        Getter for is log enabled
        :return: bool , return true if log is enabled in config file otherwise false
        """
        return self.is_log_enabled

    def create_log_file(self):
        """
        Setup basic configuration for logging
        :return:
        """
        time_stamp = time.strftime("%Y%m%d-%H%M%S")

        if LogHandler.is_log_enabled:
            if not os.path.exists('logs'):
                os.mkdir('logs')

            logging.basicConfig(filename='logs/log_hackernews_{}.txt'.format(time_stamp),
                                format='%(asctime)s - %(message)s', level=logging.DEBUG)

    @staticmethod
    def log(severity,
            message):
        """
        Log message into text file.
        :param severity: info , error , warning , exception
        :param message: text to be logged
        """
        if LogHandler.is_log_enabled:
            getattr(logging, severity)(message)
