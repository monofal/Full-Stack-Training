"""
Base class for tweets
"""


class Tweet(object):
    """
    Base class for tweets
    """

    def __init__(self,
                 tweet_text):
        self._tweet_text = tweet_text

    @property
    def tweet_text(self):
        """
        Get tweet text
        :return: string , tweet text
        """
        return self._tweet_text
