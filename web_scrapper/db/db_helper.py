"""
Databse derived class
"""

from web_scrapper.db.db_base_helper import DbBaseHelper
from web_scrapper.utils.log_handler import LogHandler


class DbHelper(DbBaseHelper):
    """
    Handle database operations
    """

    def __init__(self,
                 config_file_path):
        super(DbHelper, self).__init__(config_file_path)

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
            LogHandler.log('info', '{} new jobs added'.format(len(params)))
        except:
            LogHandler.log('exception', 'Exception while inserting records into database')
        finally:
            self.close_connection()
            self._cursor.close()

    def insert_job(self, query, params):
        """
        Insert record in database
        :param query: mysql query
        :param params: query parameters
        :return: cursor
        """
        self.open_connection()
        try:
            self._cursor.execute(query, params)
            self._connection.commit()
        except:
            LogHandler.log('exception', 'Exception while inserting record into database')
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
            LogHandler.log('exception', 'Unable to fetch records')
        finally:
            self.close_connection()
            self._cursor.close()
