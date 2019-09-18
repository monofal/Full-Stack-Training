"""
Database Handler
"""
import mysql

from web_scrapper.config import config


class DbHelper:
    __connection = None;
    __cursor = None;

    def __init__(self):
        __db_config = config['mysql'];
        self.__connection = mysql.connect(host=__db_config['host'],
                                          user=__db_config['user'],
                                          password=__db_config['password'],
                                          db=__db_config['db'],
                                          charset='utf8mb4',
                                          cursorclass=mysql.cursors.DictCursor);
        self.__cursor = self.__connection.cursor();

    def query(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor;

    def close(self):
        self.__connection.close();
