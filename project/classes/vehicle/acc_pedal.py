from project.constants.pins_ids import PinId
from project.constants.signals_ids import SignalsIds
from project.constants.acc_pedal_states import AccPedalStates
from project.constants.acc_pedal_states_v import AccPedalStatesV


class AccPedal:
    """
    Class for Acceleration pedal controlling
    """
    PIN_ID = PinId.ACC_PEDAL.value
    SIGNAL_ID = SignalsIds.ACC_PEDAL_POS
    STATES = AccPedalStates
    STATES_V = AccPedalStatesV

    @staticmethod
    def get_state_by_voltage(voltage: float) -> str:
        """
        Returns Acceleration pedal state by voltage
        Args:
            voltage (float): voltage of Acceleration pedal

        Returns:
             return (str): Acceleration pedal state
        """
        if 1.0 > voltage or voltage >= 3.5:
            return AccPedalStates.ERROR
        elif 1.0 <= voltage < 2.0:
            return AccPedalStates.POSITION_0
        elif 2.0 <= voltage < 2.5:
            return AccPedalStates.POSITION_30
        elif 2.5 <= voltage < 3.0:
            return AccPedalStates.POSITION_50
        elif 3.0 <= voltage < 3.5:
            return AccPedalStates.POSITION_100
        else:
            raise ValueError("Acceleration pedal voltage value out of accessible scope")
