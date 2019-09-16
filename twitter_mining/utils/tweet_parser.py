"""
Tweet Parser Module
"""
import re


class TweetParser(object):
    """
    Parse tweets and extract results
    """
    def __init__(self,
                 tweet_text):
        self.tweet_text = tweet_text

    def get_links(self):
        """
        Search for links in tweets
        :return: list containing links
        """
        links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.tweet_text)
        # remove any duplicates and return
        return list(set(links))

    def get_hash_tags(self):
        """
        Search for hash tags in tweets
        :return: list containing hash tags
        """
        hash_tags = re.findall(r"#(\w+)", self.tweet_text)
        # remove any duplicates and return
        return list(set(hash_tags))

    def get_mentions(self):
        """
        Search for mentions in tweets
        :return: list containing mentions
        """
        mentions = re.findall(r"@(\w+)", self.tweet_text)
        # remove any duplicates and return
        return list(set(mentions))
