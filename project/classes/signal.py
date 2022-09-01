from project.constants import signal_fields


class Signal:
    """
    Class represent instance of Signal
    """

    def __init__(self, signal_data: dict):
        self._name = signal_data[signal_fields.SIGNAL_NAME]
        self._sig_id = signal_data[signal_fields.SIGNAL_ID]
        self._value = signal_data[signal_fields.SIGNAL_VALUE]

    def __str__(self):
        return str(self.__dict__)

    @property
    def name(self) -> str:
        return self._name

    @property
    def sig_id(self) -> int:
        return self._sig_id

    @property
    def value(self) -> str:
        return self._value
