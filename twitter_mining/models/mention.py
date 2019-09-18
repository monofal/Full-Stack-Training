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
        super(Mention, self).__init__(tweet_text, "MENTIONS")
        self.extracted_result = extracted_result

