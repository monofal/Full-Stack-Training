"""
Hold tweets that fall in multiple categories
"""
from twitter_mining.models.tweet import Tweet


class Mixed(Tweet):
    """
    Hold tweets that fall in multiple categories
    """
    def __init__(self,
                 tweet_text,
                 extracted_result=None):
        super(Mixed, self).__init__(tweet_text)
        self.category_name = "MIXED"
        self.extracted_result = extracted_result

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category_name))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
