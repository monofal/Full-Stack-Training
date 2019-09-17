"""
Handle twitter api calls
"""
import tweepy
from tweepy import TweepError

from twitter_mining.response import Response


class TweetHandler(object):
    """
    Handle twitter api calls
    """

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_key,
                 access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_secret = access_secret

        auth = tweepy.auth.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(auth)

        try:
            self.api.verify_credentials()
        except TweepError as exception:
            raise Exception("Authentication failed due to : {}".format(exception))

    def search_tweets(self,
                      query,
                      tweet_count):
        """
        Search for tweets with given query and count
        :param query: search query
        :param tweet_count: total tweet count
        :return: tweet in string format
        """
        search_results = tweepy.Cursor(self.api.search,
                                       q=query,
                                       lang="en").items(tweet_count)

        return self.fill_response(search_results)

    @staticmethod
    def fill_response(search_results):
        """
        Fill response object
        :param search_results: list of tweet objects
        :return:
        """
        tweets = []
        for tweet in search_results:
            tweets.append(tweet)

        response = Response(tweets)

        return response
