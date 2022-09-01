from project.classes.pin import Pin


class Pins:
    """
    Class representing Pins instance (list of Pins instances)
    """
    def __init__(self, pins_data: list[dict]):
        self.items = []
        for pin in pins_data:
            self.items.append(Pin(pin))

    def __str__(self):
        pins_list = [str(pin_.__dict__) for pin_ in self.items]
        pins_str = '\n'.join(pins_list)
        return pins_str

    def __len__(self):
        return len(self.items)

    def __contains__(self, item: Pin):
        return item in self.items

    def __getitem__(self, item: int):
        for pin in self.items:
            if pin.pin_id == item:
                return pin

    def set_voltage(self, pin_id: int, voltage: float):
        pin = self[pin_id]
        pin.voltage = voltage

