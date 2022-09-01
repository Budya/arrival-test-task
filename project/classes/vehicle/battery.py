from project.constants.pins_ids import PinId
from project.constants.signals_ids import SignalsIds
from project.constants.battery_states import BatteryStates
from project.constants.battery_states_v import BatteryStatesV


class Battery:
    """
    Class for Battery controlling
    """
    PIN_ID = PinId.BATTERY_VOLTAGE.value
    SIGNAL_ID = SignalsIds.BATTERY_STATE
    STATES = BatteryStates
    STATES_V = BatteryStatesV

    @staticmethod
    def get_state_by_voltage(voltage: float) -> str:
        """
        Returns Battery state by voltage
        Args:
            voltage (float): voltage of Battery

        Returns:
             return (str): Battery state
        """
        if 800 >= voltage > 400:
            return Battery.STATES.READY
        elif 0 < voltage <= 400:
            return Battery.STATES.NOT_READY
        elif 0 >= voltage > 800:
            return Battery.STATES.ERROR
        else:
            raise ValueError("Battery voltage value out of accessible scope")
