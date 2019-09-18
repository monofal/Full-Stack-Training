"""
Tweet Parser Module
"""
import re

from twitter_mining.models.hash_tag import HashTag
from twitter_mining.models.link import Link
from twitter_mining.models.mention import Mention
from twitter_mining.models.mixed import Mixed
from twitter_mining.models.plain import Plain


class TweetParser(object):
    """
    Parse tweets and extract results
    """

    @staticmethod
    def get_links(tweet_text):
        """
        Search for links in tweets
        :return: list containing links
        """
        # Regular expression matches following cases
        # http: // www.foufos.gr
        # https: // www.foufos.gr
        # http: // foufos.gr
        # http: // www.foufos.gr / kino
        # http: // werer.gr
        # www.foufos.gr
        # www.mp3.com
        # www.t.co
        # http: // t.co
        # http: // www.t.co
        # https: // www.t.co
        # www.aa.com
        # http: // aa.com
        # http: // www.aa.com
        # https: // www.aa.com

        links = re.findall(r'(https?:\/\/(?:www\.|(?!www))'
                           r'[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.'
                           r'[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+'
                           r'[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www'
                           r'\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.'
                           r'[a-zA-Z0-9]+\.[^\s]{2,})', tweet_text)
        # remove any duplicates and return
        return list(set(links))

    @staticmethod
    def get_hash_tags(tweet_text):
        """
        Search for hash tags in tweets
        :return: list containing hash tags
        """
        hash_tags = re.findall(r"#(\w+)", tweet_text)
        # remove any duplicates and return
        return list(set(hash_tags))

    @staticmethod
    def get_mentions(tweet_text):
        """
        Search for mentions in tweets
        :return: list containing mentions
        """
        mentions = re.findall(r"@(\w+)", tweet_text)
        # remove any duplicates and return
        return list(set(mentions))

    @staticmethod
    def parse_and_categories(tweets):
        """
        Parse tweet text and categories accordingly
        :param tweets: tweets returned from search results
        :return: sorted list of objects of different categories of tweets
        """
        tweet_categories = []
        for tweet in tweets:
            tweet_categories.append(TweetParser.get_category_object(tweet))

        return tweet_categories

    @staticmethod
    def get_category_object(tweet):
        """
        Populate tweet list based on their category
        :param tweet: list of tweets
        :return: list of categorised tweets
        """
        links = TweetParser.get_links(tweet.text)
        hash_tags = TweetParser.get_hash_tags(tweet.text)
        mentions = TweetParser.get_mentions(tweet.text)

        if TweetParser.check_mixed_category(links, hash_tags, mentions):
            return Mixed(tweet.text)
        elif links:
            return Link(tweet.text, links)
        elif hash_tags:
            return HashTag(tweet.text, hash_tags)
        elif mentions:
            return Mention(tweet.text, mentions)
        else:
            return Plain(tweet.text)

    @staticmethod
    def check_mixed_category(*categories):
        """
        tweet is mixed if it falls in two or more categories
        """
        tweet_categories = [category for category in categories if bool(category)]
        return len(tweet_categories) >= 2
