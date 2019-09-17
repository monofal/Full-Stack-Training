"""
Hold all tweets that contains hashtags in tweet text
"""
from twitter_mining.models.tweet import Tweet


class HashTag(Tweet):
    """
    Class for hashtag category
    """
    def __init__(self,
                 tweet_text,
                 extracted_result=None):
        super(HashTag, self).__init__(tweet_text)
        self.category_name = "HASH TAG"
        self.extracted_result = extracted_result

    def show_tweet(self):
        """
        Print tweet
        """
        print("Category : {}".format(self.category_name))
        print("Tweet : {}".format(self.tweet_text.rstrip()))
