import allure
import pytest
import tests.test_data.gear_shifter_acc_pedal_td as data_for_tests
from project.classes.vehicle.vehicle import Vehicle
from framework.utils import soft_asserts
from project.steps import steps
from project.constants.description import Description


@allure.title('Test acceleration pedal and request torque')
class TestAccPedalReqTorque:
    @pytest.mark.parametrize('gear_shifter_state_drive', [Vehicle.GEAR_SHIFTER.STATES_V.DRIVE])
    @pytest.mark.parametrize('acc_pedal_state', data_for_tests.ACC_PEDAL_STATES_ACC_PEDAL_REQ_TORQUE)
    def test_gear_shifter_positive_state(self, api, gear_shifter_state_drive, acc_pedal_state):

        steps.set_gear_shifter_state(api, gear_shifter_state_drive)
        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.RELEASED)
        steps.set_acc_pedal_state(api, acc_pedal_state)
        acc_pedal_state_str = Vehicle.ACC_PEDAL.get_state_by_voltage(acc_pedal_state)
        expected_req_torque = Vehicle.REQ_TORQUE.get_state_by_acc_pedal_pos(acc_pedal_state_str)
        soft_asserts.equal(steps.get_req_torque_state(api),
                           expected_req_torque,
                           Description.REQ_TORQUE_STATE)
