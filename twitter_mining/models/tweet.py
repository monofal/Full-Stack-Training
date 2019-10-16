"""
Base class for tweets
"""


class Tweet(object):
    """
    Base class for tweets
    """

    def __init__(self,
                 tweet_text,
                 category):
        self._tweet_text = tweet_text
        self._category = category

    @property
    def tweet_text(self):
        """
        Get tweet text
        :return: string , tweet text
        """
        return self._tweet_text

    @property
    def category(self):
        """
        Get category
        :return: string , category
        """
        return self._category

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
