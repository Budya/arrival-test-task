from project.classes.vehicle.vehicle import Vehicle

GEAR_SHIFTER_STATES = Vehicle.GEAR_SHIFTER.STATES_V.STATES_LIST
ACC_PEDAL_STATES = Vehicle.ACC_PEDAL.STATES_V.STATES_LIST
REQ_TORQUE_STATE = Vehicle.REQ_TORQUE.STATES.POSITION_0
GEAR_SHIFTER_STATES_ACC_PEDAL_ERROR_GEAR_SHIFT = [Vehicle.GEAR_SHIFTER.STATES_V.DRIVE,
                                                  Vehicle.GEAR_SHIFTER.STATES_V.REVERSE]
ACC_PEDAL_STATES_BRAKE_ERR_REQ_TORQUE = [
    Vehicle.ACC_PEDAL.STATES_V.POSITION_0,
    Vehicle.ACC_PEDAL.STATES_V.POSITION_30,
    Vehicle.ACC_PEDAL.STATES_V.POSITION_50,
    Vehicle.ACC_PEDAL.STATES_V.POSITION_100,
]
