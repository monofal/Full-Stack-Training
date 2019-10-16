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
        super(Mixed, self).__init__(tweet_text, "MIXED")
        self.extracted_result = extracted_result

