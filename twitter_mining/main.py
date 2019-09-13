import os
import sys
import argparse

from twitter_mining.http.http_handler import HttpHandler


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("search_query", help="Search Query")
    parser.add_argument("tweet_count", help="Tweet Count")

    args = parser.parse_args()

    search_query = args.search_query
    tweet_count = args.tweet_count

    host = "https://api.assurestor.com/api/infrascale/monitoring/historyevents/summary"
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjRkOTc1YTJhLWFjMDktNDkwNC0zZWY1LTA4ZDczMWYxMDA2OCIsIm5iZiI6MTU2ODA2MzM3NSwiZXhwIjoxNTY4NjY4MTc1LCJpYXQiOjE1NjgwNjMzNzV9.bTLX86BpZne-5nrNbHLKjwpzG_fIsUYL0PKeFznlrTw'  # os.environ.get('API_KEY')
    request_headers = {
        "Authorization": 'Bearer ' + format(api_key),
        'Content-Type': 'application/json'
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
    response = handler.get(query_params=data)
    print(response.status_code)
    print(response.headers)
    print(response.body)


if __name__ == "__main__":
    main(sys.argv[1:])
