from requests import Response
import requests

from framework.logger.logger import Logger


class WebApi:
    """
    A class to represent WEB API functionality
    """

    CONTENT_TYPE_HEADER = 'Content-Type'
    CONTENT_TYPE_JSON = 'application/json'

    def __init__(self, base_url):
        self.__base_url = base_url

    def __base_request(self, endpoint: str, request_method, params=None, data=None, **kwargs) -> Response:
        """
        Inner base request method for using in other methods of class

        Args:
             endpoint (str): Endpoint (url)
             request_method: Request method such as get, post ...
             params: Additional necessary data for request (exmpl: request headers)
             data: Request body
             kwargs: other parameters

        Returns:
            Response object
        """
        Logger.info(f"Request - {request_method.__name__} to {endpoint}")
        if params:
            Logger.info(f"With params - {params}")
        if data:
            Logger.info(f"With data - {data}")
        resp = request_method(f"{self.__base_url}{endpoint}", params=params, data=data, **kwargs)
        Logger.info(f"Response status - {resp.status_code}")
        return resp

    def get(self, endpoint: str, **kwargs) -> Response:
        """
        Method sends request GET

        Args:
            endpoint: Request endpoint (url)
            kwargs: other parameters

        Returns:
            Response object
        """
        return self.__base_request(endpoint, requests.get, **kwargs)

    def post(self, endpoint: str, params=None, data=None, **kwargs):
        """
        Method sends request POST
        Args:
             endpoint (str): Endpoint (url)
             params: Additional necessary data for request (exmpl: request headers)
             data: Request body
             kwargs: other parameters

        Returns:
            Response object
        """
        return self.__base_request(endpoint, requests.post, params=params, data=data, **kwargs)
