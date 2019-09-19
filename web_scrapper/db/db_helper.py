"""
Databse derived class
"""
import json
import logging

from web_scrapper.db.db_base_helper import DbBaseHelper
from web_scrapper.model.job import Job
from web_scrapper.utils.log_handler import LogHandler


class DbHelper(DbBaseHelper):
    """
    Handle database operations
    """

    def bulk_insertion(self, query, params):
        """
        Insert multiple jobs into database
        :param query: mysql query
        :param params: query parameters
        :return: cursor
        """
        self.open_connection()
        try:
            self._cursor.executemany(query, params)
            self._connection.commit()
            if LogHandler.is_log_enabled:
                logging.info("{} new jobs added".format(len(params)))
        except:
            if LogHandler.is_log_enabled:
                logging.exception("Unable to insert data into database")
        finally:
            self.close_connection()
            self._cursor.close()

    def execute_query(self,
                      query):
        """
        Get recently added job list
        :param query: mysql query
        :return: cursor
        """
        self.open_connection()
        try:
            self._cursor.execute(query)
            records = self._cursor.fetchall()

            return records
        except:
            if LogHandler.is_log_enabled:
                logging.exception("Unable to fetch records")
        finally:
            self.close_connection()
            self._cursor.close()
