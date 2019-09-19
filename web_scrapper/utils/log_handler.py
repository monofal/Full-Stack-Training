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
    __log_file = None

    def __init__(self):
        time_stamp = time.strftime("%Y%m%d-%H%M%S")

        if LogHandler.is_log_enabled:
            if not os.path.exists('logs'):
                os.mkdir('logs')

            logging.basicConfig(filename='logs/log_hackernews_{}.txt'.format(time_stamp),
                                format='%(asctime)s - %(message)s', level=logging.DEBUG)

    @property
    def get_log_file(self):
        """
        Getter for log file
        :return: file pointer
        """
        return self.__log_file

    @property
    def is_enabled(self):
        """
        Getter for is log enabled
        :return: bool , return true if log is enabled in config file otherwise false
        """
        return self.is_log_enabled

    def close_log_file(self):
        """
        Close log file
        """
        if not self.is_log_enabled:
            self.__log_file.close()
