"""
Hold all tweets that contains mentions in tweet text
"""
from twitter_mining.models.tweet import Tweet


class Mention(Tweet):
    """
    Class for mention category
    """
    def __init__(self,
                 tweet_text,
                 extracted_result=None):
        super(Mention, self).__init__(tweet_text)
        self.category_name = "MENTIONS"
        self.extracted_result = extracted_result

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category_name))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
