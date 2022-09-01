from project.classes.signal import Signal
from project.constants.acc_pedal_states import AccPedalStates
from project.constants.signals_ids import SignalsIds
from project.constants.req_torque_states import ReqTorqueStates


class RequestTorque:
    """
    Class for Request torque controlling
    """
    SIGNAL_ID = SignalsIds.REQ_TORQUE
    STATES = ReqTorqueStates

    @staticmethod
    def get_state_by_acc_pedal_pos(acc_pedal_position: str):
        """
        Returns Request torque state by Acceleration pedal state
        Args:
            acc_pedal_position (str): position of Acceleration pedal

        Returns:
             return (str): Request torque state
        """
        match acc_pedal_position:
            case AccPedalStates.ERROR:
                return ReqTorqueStates.ERROR
            case AccPedalStates.POSITION_0:
                return ReqTorqueStates.POSITION_0
            case AccPedalStates.POSITION_30:
                return ReqTorqueStates.POSITION_30
            case AccPedalStates.POSITION_50:
                return ReqTorqueStates.POSITION_50
            case AccPedalStates.POSITION_100:
                return ReqTorqueStates.POSITION_100

    @staticmethod
    def get_signal_state() -> str:
        """
        Returns remote Request torque state signal

        Returns:
             Current Request torque state signal (str)
        """
        signal = Signal(RequestTorque.SIGNAL_ID)
        return signal.value
