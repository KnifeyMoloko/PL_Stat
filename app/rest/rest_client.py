"""
REST client class for the PL_Stat app.
Author: Maciej Cisowski
"""
import requests
import json
from logging import getLogger


logger = getLogger("rest.RestClient")


class RestClient(object):
    def __init__(self, ssl: bool, api_key: str):
        """
        Create a rest client instance for making http/s requests.
        :param ssl: should the client work in SSL mode or not
        :param api_key: optional for working with APIs needing keys
        """
        self.url_prefix = "https://" if ssl else "http://"
        self.host = "bdl.stat.gov.pl"
        self.endpoint = "/api/v1/"
        self.__api_key = api_key

    def get(self, resource_path: str) -> requests.Response:
        """
        Sends a GET method request to the host resource specified
        by the resource path. Returns a JSON type response and throws
        a ConnectionError in case of problems.
        :param resource_path: string with the path to the resource
        :return: request response
        :rtype: json
        """
        # construct request headers
        headers = {"X-ClientId": self.__api_key,
                   "Host": "bdl.stat.gov.pl",
                   "Content-Type": "application/json"}

        # construct url string
        url = f"{self.url_prefix}{self.host}{self.endpoint}{resource_path}"

        logger.info(f"Attempting a GET request for: {url}")
        return requests.get(url=url,
                            params={},
                            headers=headers)
