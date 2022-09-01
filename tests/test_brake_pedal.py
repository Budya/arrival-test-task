import allure
import pytest

import tests.test_data.brake_pedal_td as data_for_tests

from project.classes.vehicle.vehicle import Vehicle
from framework.utils import soft_asserts
from project.constants.description import Description
from project.steps import steps


class TestBattery:
    @allure.title('Test brake pedal in state "Pressed"')
    @pytest.mark.parametrize('gear_shifter_state', data_for_tests.GEAR_SHIFTER_STATES)
    @pytest.mark.parametrize('acc_pedal_state', data_for_tests.ACC_PEDAL_STATES)
    def test_brake_pedal_state_pressed(self, api,  gear_shifter_state, acc_pedal_state):
        steps.set_gear_shifter_state(api, gear_shifter_state)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_shifter_state),
                           Description.GEAR_POSITION)

        steps.set_acc_pedal_state(api, acc_pedal_state)

        soft_asserts.equal(steps.get_acc_pedal_state(api),
                           Vehicle.ACC_PEDAL.get_state_by_voltage(acc_pedal_state),
                           Description.ACC_PEDAL_STATE)
        soft_asserts.equal(steps.get_req_torque_state(api),
                           data_for_tests.REQ_TORQUE_STATE,
                           Description.ACC_PEDAL_STATE)

    @allure.title('Test brake pedal in state "Released"')
    @pytest.mark.parametrize('acc_pedal_state', data_for_tests.ACC_PEDAL_STATES)
    @pytest.mark.parametrize('gear_shifter_state', data_for_tests.GEAR_SHIFTER_STATES)
    def test_brake_pedal_state_released(self, api, gear_shifter_state, acc_pedal_state):
        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.RELEASED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.RELEASED,
                           Description.BRAKE_PEDAL_STATE)
        expected_gear_shifter_state = steps.get_gear_shifter_state(api)
        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_shifter_state))
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           expected_gear_shifter_state,
                           Description.GEAR_POSITION)

        steps.set_acc_pedal_state(api, acc_pedal_state)
        soft_asserts.equal(steps.get_req_torque_state(api),
                           data_for_tests.REQ_TORQUE_STATE,
                           Description.REQ_TORQUE_STATE)

    @allure.title('Test brake pedal and gear shifter when brake pedal in state "Error"')
    @pytest.mark.parametrize('gear_shifter_state', data_for_tests.GEAR_SHIFTER_STATES_ACC_PEDAL_ERROR_GEAR_SHIFT)
    def test_brake_pedal_state_error_gear_shift(self, api, gear_shifter_state):
        steps.set_gear_shifter_state(api, gear_shifter_state)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_shifter_state),
                           Description.GEAR_POSITION)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.ERROR)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.ERROR,
                           Description.BRAKE_PEDAL_STATE)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.NEUTRAL,
                           Description.GEAR_POSITION)

    @allure.title('Test brake pedal and request torque with brake pedal state "Error"')
    @pytest.mark.parametrize('gear_shifter_state', data_for_tests.GEAR_SHIFTER_STATES_ACC_PEDAL_ERROR_GEAR_SHIFT)
    @pytest.mark.parametrize('acc_pedal_state', data_for_tests.ACC_PEDAL_STATES_BRAKE_ERR_REQ_TORQUE)
    def test_brake_pedal_state_error_req_torque(self, api, gear_shifter_state, acc_pedal_state):
        steps.set_gear_shifter_state(api, gear_shifter_state)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_shifter_state),
                           Description.GEAR_POSITION)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.RELEASED)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.RELEASED,
                           Description.BRAKE_PEDAL_STATE)

        steps.set_acc_pedal_state(api, acc_pedal_state)

        acc_pedal_position = Vehicle.ACC_PEDAL.get_state_by_voltage(acc_pedal_state)
        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.get_state_by_acc_pedal_pos(acc_pedal_position),
                           Description.REQ_TORQUE_STATE)

        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.ERROR)

        soft_asserts.equal(steps.get_brake_pedal_state(api),
                           Vehicle.BRAKE_PEDAL.STATES.ERROR,
                           Description.BRAKE_PEDAL_STATE)
        soft_asserts.equal(steps.get_req_torque_state(api),
                           Vehicle.REQ_TORQUE.STATES.POSITION_0,
                           Description.REQ_TORQUE_STATE)
