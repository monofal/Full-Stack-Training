"""
Hold tweets that does not fall in any category
"""
from twitter_mining.models.tweet import Tweet


class Plain(Tweet):
    """
    Hold tweets that do not fall in any categories
    """
    def __init__(self,
                 tweet_text,
                 extracted_result=None):
        super(Plain, self).__init__(tweet_text)
        self.category_name = "PLAIN"
        self.extracted_result = extracted_result

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category_name))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
