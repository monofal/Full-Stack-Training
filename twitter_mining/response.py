"""
Api Response
"""


class Response(object):
    """
    Hold response returned from tweepy api
    """

    def __init__(self,
                 tweets,
                 status_code=None):
        self._status_code = status_code
        self.__tweets = tweets

    @property
    def status_code(self):
        """
        :return: int, status code
        """
        return self._status_code

    @property
    def tweets(self):
        """
        :return: tweet object
        """
        return self.__tweets
