from project.constants.pins_ids import PinId
from project.constants.gear_shifter_states import GearShifterStates
from project.constants.gear_shifter_states_v import GearShifterStatesV
from project.constants.signals_ids import SignalsIds


class GearShifter:
    """
    Class for Gear shifter controlling
    """
    PIN_1_ID = PinId.GEAR_1.value
    PIN_2_ID = PinId.GEAR_2.value
    SIGNAL_ID = SignalsIds.GEAR_POSITION
    STATES = GearShifterStates
    STATES_V = GearShifterStatesV

    @staticmethod
    def get_state_by_voltage(voltage: tuple[float, float]):
        """
        Returns Gear shifter state by voltage

        Args:
            voltage (tuple[float, float]): voltage of Gear shifter

        Returns:
             return (str): Gear shifter state
        """
        if voltage[0] == 0.67 and voltage[1] == 3.12:
            return GearShifter.STATES.PARK
        elif voltage[0] == 1.48 and voltage[1] == 2.28:
            return GearShifter.STATES.NEUTRAL
        elif voltage[0] == 2.28 and voltage[1] == 1.48:
            return GearShifter.STATES.REVERSE
        elif voltage[0] == 3.12 and voltage[1] == 0.67:
            return GearShifter.STATES.DRIVE
