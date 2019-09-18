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
        super(Link, self).__init__(tweet_text, "LINK")
        self.extracted_result = extracted_result

