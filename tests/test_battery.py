import allure
import pytest

import tests.test_data.battery_td as data_for_tests

from project.classes.vehicle.battery import Battery
from project.classes.vehicle.vehicle import Vehicle
from framework.utils import soft_asserts
from project.constants.description import Description
from project.steps import steps


class TestBattery:
    @allure.title('Test battery in state "Ready"')
    @pytest.mark.parametrize('test_data', data_for_tests.BATTERY_STATE_READY_TEST_DATA)
    def test_battery_state_ready(self, api, test_data):
        steps.set_battery_state(api, test_data)
        current_voltage = api.pins.get_pin(Vehicle.BATTERY.PIN_ID).voltage
        current_state = steps.get_battery_state(api)

        soft_asserts.equal(current_voltage, test_data, Description.BATT_VOLTAGE)
        soft_asserts.equal(current_state, Battery.STATES.READY, Description.BATT_STATE)

    @allure.title('Test battery in state "Not Ready"')
    @pytest.mark.parametrize('test_data', data_for_tests.BATTERY_STATE_NOT_READY_TEST_DATA)
    def test_battery_state_not_ready(self, api, test_data):
        steps.set_battery_state(api, test_data)
        current_voltage = api.pins.get_pin(Vehicle.BATTERY.PIN_ID).voltage
        current_state = steps.get_battery_state(api)

        soft_asserts.equal(current_voltage, test_data, Description.BATT_VOLTAGE)
        soft_asserts.equal(current_state, Battery.STATES.NOT_READY, Description.BATT_STATE)

    @allure.title('Test battery in state "Error"')
    @pytest.mark.parametrize('test_data', data_for_tests.BATTERY_STATE_ERROR_TEST_DATA)
    def test_battery_state_error(self, api, test_data):
        steps.set_battery_state(api, test_data)
        current_voltage = api.pins.get_pin(Vehicle.BATTERY.PIN_ID).voltage
        current_state = steps.get_battery_state(api)

        soft_asserts.equal(current_voltage, test_data, Description.BATT_VOLTAGE)
        soft_asserts.equal(current_state, Battery.STATES.ERROR, Description.BATT_STATE)

    @allure.title('Test system when battery in state "Not Ready"')
    @pytest.mark.parametrize('battery_pin_value', [0.01])
    @pytest.mark.parametrize('gear_position', [Vehicle.GEAR_SHIFTER.STATES_V.DRIVE,
                                               Vehicle.GEAR_SHIFTER.STATES_V.REVERSE])
    def test_system_battery_state_not_ready(self, api, battery_pin_value, gear_position):
        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.PRESSED)
        steps.set_gear_shifter_state(api, gear_position)
        current_brake_pedal = steps.get_brake_pedal_state(api)
        current_gear = steps.get_gear_shifter_state(api)
        expected_gear_position = Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_position)

        soft_asserts.equal(current_brake_pedal, Vehicle.BRAKE_PEDAL.STATES.PRESSED, Description.BRAKE_PEDAL_STATE)
        soft_asserts.equal(current_gear, expected_gear_position, Description.GEAR_POSITION)

        steps.set_battery_state(api, battery_pin_value)
        current_battery_voltage = api.pins.get_pin(Vehicle.BATTERY.PIN_ID).voltage
        current_battery_state = steps.get_battery_state(api)
        current_gear = steps.get_gear_shifter_state(api)

        soft_asserts.equal(current_battery_voltage, battery_pin_value, Description.BATT_VOLTAGE)
        soft_asserts.equal(current_battery_state, Vehicle.BATTERY.STATES.NOT_READY, Description.BATT_STATE)
        soft_asserts.equal(current_gear, Vehicle.GEAR_SHIFTER.STATES.NEUTRAL, Description.GEAR_POSITION)

        steps.set_gear_shifter_state(api, gear_position)

        current_gear = steps.get_gear_shifter_state(api)
        soft_asserts.equal(current_gear, Vehicle.GEAR_SHIFTER.STATES.NEUTRAL, Description.GEAR_POSITION)

    @allure.title('Test system when battery state "Error"')
    @pytest.mark.parametrize('error_pin_value', data_for_tests.SYS_BATTERY_STATE_ERROR)
    def test_system_battery_state_error(self, api, error_pin_value):
        battery_signal = Vehicle.BATTERY.STATES.ERROR
        gear_position_signal = Vehicle.GEAR_SHIFTER.STATES.NEUTRAL
        gear_pin_1_voltage = 0
        gear_pin_2_voltage = 0
        brake_pedal_signal = Vehicle.BRAKE_PEDAL.STATES.ERROR
        brake_pedal_pin = 0
        acc_pedal_signal = Vehicle.ACC_PEDAL.STATES.ERROR
        acc_pedal_pin = 0
        req_torque_state = Vehicle.REQ_TORQUE.STATES.POSITION_0

        steps.set_battery_state(api, error_pin_value)

        soft_asserts.equal(steps.get_battery_state(api), battery_signal, Description.BATT_STATE)
        soft_asserts.equal(steps.get_gear_shifter_state(api), gear_position_signal, Description.GEAR_POSITION)
        soft_asserts.equal(api.pins.get_pin(Vehicle.GEAR_SHIFTER.PIN_1_ID).voltage,
                           gear_pin_1_voltage,
                           Description.GEAR_SH_PIN_1)
        soft_asserts.equal(api.pins.get_pin(Vehicle.GEAR_SHIFTER.PIN_1_ID).voltage,
                           gear_pin_2_voltage,
                           Description.GEAR_SH_PIN_2)
        soft_asserts.equal(steps.get_brake_pedal_state(api), brake_pedal_signal, Description.BRAKE_PEDAL_STATE)
        soft_asserts.equal(api.pins.get_pin(Vehicle.BRAKE_PEDAL.PIN_ID).voltage,
                           brake_pedal_pin,
                           Description.BRAKE_PEDAL_VOLTAGE)
        soft_asserts.equal(steps.get_acc_pedal_state(api), acc_pedal_signal, Description.ACC_PEDAL_STATE)
        soft_asserts.equal(api.pins.get_pin(Vehicle.ACC_PEDAL.PIN_ID).voltage, acc_pedal_pin, Description.ACC_PEDAL_VOLTAGE)
        soft_asserts.equal(steps.get_req_torque_state(api), req_torque_state, Description.REQ_TORQUE_STATE)
