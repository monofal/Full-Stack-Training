"""
Databse derived class
"""
import json

from pip._internal.utils import logging

from web_scrapper.db.db_base_helper import DbBaseHelper


class DbHelper(DbBaseHelper):
    """
    Handle database operations
    """

    def __init__(self):
        config = self.get_db_credentials()
        super(DbHelper, self).__init__(config)

    @staticmethod
    def get_db_credentials():
        try:
            with open('config.json') as config:
                mysql_config = json.load(config)
        except FileNotFoundError:
            print('Error')

        return mysql_config

    def bulk_insertion(self, query, params):
        """
        Insert multiple jobs into database
        :param query: mysql query
        :param params: query parameters
        :return: cursor
        """
        self.open_connection()
        cursor = self._connection.cursor()
        try:
            self._cursor.executemany(query, params)
            self._connection.commit()
        except:
            logging.warn("Failed to insert values {}".format(params))
        finally:
            cursor.close()

    def insert_job(self, query, params):
        """
        Insert jobs into database
        :param query: mysql query
        :param params: query parameters
        :return: cursor
        """
        self.open_connection()
        cursor = self._connection.cursor()
        try:
            self._cursor.execute(query, params)
            self._connection.commit()
        except:
            logging.warn("Failed to insert values {}".format(params))
        finally:
            cursor.close()
