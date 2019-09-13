"""
Handle api responses
"""
import json


class Response(object):
    """Holds the response from an API call."""

    def __init__(self, response):
        """
        :param response: The return value from a open call
                         on a urllib.build_opener()
        :type response:  urllib response object
        """
        self._status_code = response.getcode()
        self._body = response.read()
        self._headers = response.info()

    @property
    def status_code(self):
        """
        :return: integer, status code of API call
        """
        return self._status_code

    @property
    def body(self):
        """
        :return: response from the API
        """
        return self._body

    @property
    def headers(self):
        """
        :return: dict of response headers
        """
        return self._headers

    @property
    def to_dict(self):
        """
        :return: dict of response from the API
        """
        if self.body:
            return json.loads(self.body.decode('utf-8'))
        else:
            return None
