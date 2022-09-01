from project.classes.vehicle.acc_pedal import AccPedal
from project.classes.vehicle.battery import Battery
from project.classes.vehicle.brake_pedal import BrakePedal
from project.classes.vehicle.gear_shifter import GearShifter
from project.classes.vehicle.req_torque import RequestTorque


class Vehicle:
    """
    Class wrapper for storing and controlling all system components
    """
    BATTERY = Battery
    ACC_PEDAL = AccPedal
    BRAKE_PEDAL = BrakePedal
    GEAR_SHIFTER = GearShifter
    REQ_TORQUE = RequestTorque
