import json

from framework.api.web_api import WebApi
from project.classes.pin import Pin
from project.classes.pins import Pins
from project.config import GET_PINS_END_POINT, UPDATE_PIN_ENDPOINT, UPDATE_PINS_ENDPOINT
from project.constants import pin_fields


class PinsApi:
    """
    Class to represent manipulation with Pin objects via WEB API
    """

    def __init__(self, base_url):
        self._base_url = base_url
        self.__API = WebApi(self._base_url)

    def get_pin(self, pin_id: int):
        """
        Returns Pin instance

        Args:
            pin_id (int)

        Returns:
             Instance of Pin
        """
        pin = self.__API.get(f"{GET_PINS_END_POINT}/{pin_id}").json()
        return Pin(pin)

    def get_pins(self):
        """
        Returns Pins instance

        Returns:
             Instance of Pins
        """
        pins_data = self.__API.get(f"{GET_PINS_END_POINT}").json()
        return Pins(pins_data)

    def update_pin(self, pin_id: int, voltage: float):
        """
        Updates Pin instance

        Args:
            pin_id (int): target pin_id for update
            voltage (float): value for update
        """
        body = {pin_fields.PIN_VOLTAGE: voltage}
        self.__API.post(endpoint=f"{UPDATE_PIN_ENDPOINT.format(pin_id)}", data=body)

    def update_pins(self, pins: Pins):
        """
        Update list of Pins with one POST request

        Args:
            pins (Pins class instance): pins list which values will be updated
        """
        data_dict = {"Pins": []}
        for pin in pins.items:
            data_dict["Pins"].append(dict({"PinId": pin.pin_id, "Voltage": pin.voltage}))
        body = json.dumps(data_dict)
        self.__API.post(endpoint=f"{UPDATE_PINS_ENDPOINT}",
                        headers={self.__API.CONTENT_TYPE_HEADER: self.__API.CONTENT_TYPE_JSON}, data=body)
