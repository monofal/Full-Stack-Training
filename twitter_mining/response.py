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
        self._tweets = tweets

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
        return self._tweets

    def get_tweet_text(self):
        """
        Concatenate tweet text in a single string for parsing
        :return: string , tweets text
        """
        tweet_text = ''
        for tweet in self.tweets:
            tweet_text += tweet.text

        return tweet_text
