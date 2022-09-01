from project.classes.api.pins_api import PinsApi
from project.classes.api.signals_api import SignalsApi


class VehicleApi:
    """
    Class wrapper for storing other API classes
    """
    def __init__(self, base_url):
        self._base_url = base_url
        self._pins = PinsApi(self._base_url)
        self._signals = SignalsApi(self._base_url)

    @property
    def pins(self):
        return self._pins

    @property
    def signals(self):
        return self._signals
