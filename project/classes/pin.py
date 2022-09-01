from project.constants import pin_fields


class Pin:
    """
    Class representing Pin instance
    """
    def __init__(self, pin_data: dict):
        self._name = pin_data[pin_fields.PIN_NAME]
        self._pin_id = pin_data[pin_fields.PIN_ID]
        self._voltage = pin_data[pin_fields.PIN_VOLTAGE]

    def __str__(self):
        return str(self.__dict__)

    @property
    def name(self) -> str:
        return self._name

    @property
    def pin_id(self) -> int:
        return self._pin_id

    @property
    def voltage(self) -> float:
        return self._voltage

    @voltage.setter
    def voltage(self, voltage: float):
        self._voltage = voltage
