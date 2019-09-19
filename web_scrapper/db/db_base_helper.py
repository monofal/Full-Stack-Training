"""
Database base Handler
"""
import mysql.connector


class DbBaseHelper(object):
    """
    Handle database operations
    """
    _connection = None
    _cursor = None

    def __init__(self,
                 config):
        _db_config = config['mysql']

    def open_connection(self):
        try:
            self._connection = mysql.connector.connect(host=self._db_config['host'],
                                                       user=self._db_config['user'],
                                                       password=self.db_config['password'],
                                                       db=self._db_config['db'])
            if self._connection.is_connected():
                self._cursor = self._connection.cursor()
        except:
            print('Error')

    def close_connection(self):
        """
        Close database connection
        """
        self._connection.close()
