import allure

from framework.utils import soft_asserts
from project.classes.vehicle.vehicle import Vehicle
from project.constants.description import Description
from project.steps import steps


@allure.title('End to End vehicle test')
class TestVehicleE2E:
    def test_vehicle_e_2_e(self, api):
        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.DRIVE)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.DRIVE,
                           Description.GEAR_POSITION)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.RELEASED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.RELEASED,
                           Description.BRAKE_PEDAL_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_30)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_30,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_30,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_50)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_50,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_50,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_100)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_100,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_100,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_0)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_0,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_0,
                           Description.REQ_TORQUE_STATE)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.PRESSED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.PRESSED,
                           Description.BRAKE_PEDAL_STATE)

        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.REVERSE)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.REVERSE,
                           Description.GEAR_POSITION)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.RELEASED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.RELEASED,
                           Description.BRAKE_PEDAL_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_30)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_30,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_30,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_50)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_50,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_50,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_100)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_100,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_100,
                           Description.REQ_TORQUE_STATE)

        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_0)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.STATES.POSITION_0,
                           Description.ACC_PEDAL_STATE)

        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_0,
                           Description.REQ_TORQUE_STATE)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.PRESSED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.PRESSED,
                           Description.BRAKE_PEDAL_STATE)

        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.PARK)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.PARK,
                           Description.GEAR_POSITION)





