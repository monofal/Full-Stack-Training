"""
Main Module
"""

import argparse
import os

from twitter_mining.utils.tweet_parser import TweetParser
from twitter_mining.tweet_handler.tweet_handler import TweetHandler
from twitter_mining.utils.utility import Utility


def parse_arguments():
    """
    Parse command line arguments
    :return: query and tweet count extracted from command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search_query", help="Search Query",
                        type=str, required=True)
    parser.add_argument("-n", "--tweet_count", help="Tweet Count",
                        type=Utility.validate_tweet_count, required=True)

    args = parser.parse_args()

    return args.search_query, args.tweet_count


def start_mining(search_query,
                 tweet_count):
    """
    Start mining tweets from twitter
    :param search_query: search parameter
    :param tweet_count: total tweet count
    """
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_key = os.environ.get('ACCESS_KEY')
    access_secret = os.environ.get('ACCESS_SECRET')

    # Check for null values
    Utility.validate_user_credentials(consumer_key, consumer_secret, access_key, access_secret)

    tweet_handler = TweetHandler(consumer_key, consumer_secret, access_key, access_secret)
    response = tweet_handler.search_tweets(search_query, tweet_count)

    tweet_categories = TweetParser.parse_and_categories(response.tweets)
    show_tweets(tweet_categories)


def show_tweets(tweet_categories):
    """
    Show tweets
    """
    for tweet in tweet_categories:
        tweet.show_tweet()


def main():
    """
    App entry point
    :return:
    """
    search_query, tweet_count = parse_arguments()
    start_mining(search_query, tweet_count)


if __name__ == "__main__":
    main()
