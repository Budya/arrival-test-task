import allure
import pytest

import tests.test_data.gear_shifter_positive_stage_td as data_for_tests

from project.classes.vehicle.vehicle import Vehicle
from framework.utils import soft_asserts
from project.constants.description import Description
from project.steps import steps


class TestGearShifter:
    @allure.title('Test gear shifter in positive states')
    @pytest.mark.parametrize('gear_shifter_state', data_for_tests.GEAR_SHIFTER_STATES)
    def test_gear_shifter_positive_state(self, api, gear_shifter_state):
        steps.set_gear_shifter_state(api, gear_shifter_state)
        expected_gear_shifter_state = Vehicle.GEAR_SHIFTER.get_state_by_voltage(gear_shifter_state)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           expected_gear_shifter_state,
                           Description.GEAR_POSITION)

    @allure.title('Test gear shifter when battery in "Error" state')
    def test_gear_shifter_battery_error(self, api):
        steps.set_battery_state(api, Vehicle.BATTERY.STATES_V.ERROR)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.NEUTRAL,
                           Description.GEAR_POSITION)

        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.DRIVE)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.NEUTRAL,
                           Description.GEAR_POSITION)

    @allure.title('Test gear shifter when brake pedal in "Error" state')
    def test_gear_shifter_brake_pedal_error(self, api):
        gear_shifter_state = steps.get_gear_shifter_state(api)
        steps.set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.ERROR)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           gear_shifter_state,
                           Description.GEAR_POSITION)

        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.DRIVE)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.PARK,
                           Description.GEAR_POSITION)

    @allure.title('Test gear shifter when acceleration pedal in "Error" state')
    def test_gear_shifter_acc_pedal_error(self, api):
        steps.set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.ERROR)

        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.NEUTRAL,
                           Description.GEAR_POSITION)

        steps.set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.DRIVE)
        soft_asserts.equal(steps.get_gear_shifter_state(api),
                           Vehicle.GEAR_SHIFTER.STATES.NEUTRAL,
                           Description.GEAR_POSITION)
