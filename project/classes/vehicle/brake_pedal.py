from project.constants.pins_ids import PinId
from project.constants.brake_pedal_states import BrakePedalStates
from project.constants.brake_pedal_states_v import BrakePedalStatesV
from project.constants.signals_ids import SignalsIds


class BrakePedal:
    """
    Class for Brake pedal controlling
    """
    PIN_ID = PinId.BRAKE_PEDAL.value
    SIGNAL_ID = SignalsIds.BRAKE_PEDAL_POS
    STATES = BrakePedalStates
    STATES_V = BrakePedalStatesV

    @staticmethod
    def get_state_by_voltage(voltage: float):
        """
        Returns Brake pedal state by voltage
        Args:
            voltage (float): voltage of Brake pedal

        Returns:
             return (str): Brake pedal state
        """
        if 1 > voltage >= 3:
            return BrakePedalStates.ERROR
        elif 1 <= voltage < 2:
            return BrakePedalStates.PRESSED
        elif 2 <= voltage < 3:
            return BrakePedalStates.RELEASED
        else:
            raise ValueError("Brake pedal voltage value out of accessible scope")
