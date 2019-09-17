"""
Utility Module
"""
import argparse


class Utility(object):
    """
    Utility class
    """

    @staticmethod
    def validate_user_credentials(consumer_key,
                                  consumer_secret,
                                  access_key,
                                  access_secret):
        """
        Check if user credentials are not null
        :return: raise exception if keys are invalid
        """
        if consumer_key is None or \
                consumer_secret is None or \
                access_key is None or \
                access_secret is None:
            raise Exception('Invalid credentials.')

    @staticmethod
    def validate_tweet_count(count):
        """
        Validate that tweet count is positive integer value
        :param count: tweet count
        """
        try:
            tweet_count = int(count)
        except ValueError:
            raise argparse.ArgumentTypeError("%s is not valid integer" % count)

        if tweet_count <= 0:
            raise argparse.ArgumentTypeError("%s is not valid positive integer" % count)
        return tweet_count
