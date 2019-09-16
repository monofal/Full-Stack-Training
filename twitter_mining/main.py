"""
Main Module
"""

import argparse
import os

from twitter_mining.utils.tweet_parser import TweetParser
from twitter_mining.tweet_handler.TweetHandler import TweetHandler


def parse_arguments():
    """
    Parse command line arguments
    :return: query and tweet count extracted from command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search_query", help="Search Query",
                        type=str, required=True)
    parser.add_argument("-n", "--tweet_count", help="Tweet Count",
                        type=validate_count, required=True)

    args = parser.parse_args()

    return args.search_query, args.tweet_count


def validate_count(count):
    """
    Validate that tweet count is positive integer value
    :param count: tweet count
    """
    try:
        tweet_count = int(count)
        if tweet_count <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % count)
        return tweet_count
    except ValueError:
        raise ValueError("Invalid input")


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

    tweet_handler = TweetHandler(consumer_key, consumer_secret, access_key, access_secret)
    response = tweet_handler.search_tweets(search_query, tweet_count)
    tweet_text = response.get_tweet_text()

    parse_tweets(tweet_text)


def parse_tweets(search_results):
    """
    Parse tweets to extract links hashtags and mentions
    :param search_results: tweet text in a single string
    """
    parser = TweetParser(search_results)
    print('Hash Tags {}'.format(parser.get_hash_tags()))
    print('links {}'.format(parser.get_links()))
    print('mentions {}'.format(parser.get_mentions()))


def main():
    """
    App entry point
    :return:
    """
    search_query, tweet_count = parse_arguments()
    start_mining(search_query, tweet_count)


if __name__ == "__main__":
    main()
