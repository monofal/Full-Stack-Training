"""
Hold all tweets that contains links in tweet text
"""
from twitter_mining.models.tweet import Tweet


class Link(Tweet):
    """
        Class for hashtag category
    """
    def __init__(self,
                 tweet_text,
                 extracted_result=None):
        super(Link, self).__init__(tweet_text)
        self.category_name = "LINK"
        self.extracted_result = extracted_result

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category_name))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
