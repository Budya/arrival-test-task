from framework.api.web_api import WebApi
from project.classes.signal import Signal
from project.classes.signals import Signals
from project.config import GET_SIGNALS_ENDPOINT


class SignalsApi:
    """
    Class wrapper for manipulating Signal instances via WEB API
    """

    def __init__(self, base_url):
        self._base_url = base_url
        self.__API = WebApi(self._base_url)

    def get_signal(self, signal_id: int):
        """
        Returns Signal instance

        Args:
            signal_id (int): signal id for fetching data

        Returns:
            Signal instance
        """
        signal_data = self.__API.get(f"{GET_SIGNALS_ENDPOINT}/{signal_id}").json()
        return Signal(signal_data)

    def get_signals(self):
        """
        Returns Signals instance

        Returns:
            SignalS instance
        """
        signals_data = self.__API.get(f"{GET_SIGNALS_ENDPOINT}").json()
        return Signals(signals_data)
