import os
import sys
import argparse

from twitter_mining.http.http_handler import HttpHandler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_query", help="Search Query")
    parser.add_argument("tweet_count", help="Tweet Count")

    args = parser.parse_args()

    search_query = args.search_query
    tweet_count = args.tweet_count

    host = "https://api.twitter.com/1.1/search/tweets.json?q=from%3Atwitterdev&result_type=mixed&count=2"
    api_key = 'ria2kzrCoUlnMgrrDXWZmfeLeconsumerSecretKey=U7HPFUFQsgZSDaB1OJQ7Hx4vIasVJw9fqlQdIOEKXnd2TL3nLTaccessToken=1013682218101768192-WLU00n8Sh1Ku09I0rupZquybz0qIw2accessTokenSecret=Hra6GzKLYEIvTHGBAPGS733UJFOuPhydtgxzw8kPzhrR8'  # os.environ.get('API_KEY')
    request_headers = {
        'authorization': 'OAuth oauth_consumer_key=' + format(api_key),
        'oauth_nonce' : 'generated-nonce',
        'oauth_signature' : 'generated-signature',
        'oauth_signature_method' : 'HMAC-SHA1',
        'oauth_timestamp' : 'generated-timestamp',
        'oauth_token' : 'access-token-for-authed-user',
        'oauth_version' : '1.0'
    }




    data = {
        "period": "last24h",
        "accountType": '1'
    }
    # version = 3  # we could also use client.version(3)
    handler = HttpHandler(host=host,
                          request_headers=request_headers,
                          version=None)

    # GET collection
    response = handler.get()
    print(response.status_code)
    print(response.headers)
    print(response.body)


if __name__ == "__main__":
    main()
