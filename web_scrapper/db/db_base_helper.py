"""
Database base Handler
"""

import mysql.connector

from web_scrapper.utils.log_handler import LogHandler
from web_scrapper.utils.utility import Utility


class DbBaseHelper(object):
    """
    Handle database operations
    """
    _connection = None
    _cursor = None

    def __init__(self):
        self._db_config = Utility.get_db_credentials()

    def open_connection(self):
        """
        Open database connection
        """
        try:
            self._connection = mysql.connector.connect(host=self._db_config['host'],
                                                       user=self._db_config['user'],
                                                       password=self._db_config['password'],
                                                       db=self._db_config['db'])
            if self._connection.is_connected():
                self._cursor = self._connection.cursor()
        except:
            LogHandler.log('exception', 'Unable to open database connection')

    def close_connection(self):
        """
        Close database connection
        """
        if self._connection.is_connected():
            self._connection.close()
