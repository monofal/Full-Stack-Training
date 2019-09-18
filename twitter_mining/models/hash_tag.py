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
        super(HashTag, self).__init__(tweet_text, "HASH TAG")
        self.extracted_result = extracted_result
