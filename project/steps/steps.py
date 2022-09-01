import allure

from project.classes.api.vehicle_api import VehicleApi
from project.classes.vehicle.vehicle import Vehicle


@allure.step('Reset system state')
def reset_system_state(api: VehicleApi):
    set_battery_state(api, Vehicle.BATTERY.STATES_V.READY)
    set_acc_pedal_state(api, Vehicle.ACC_PEDAL.STATES_V.POSITION_0)
    set_brake_pedal_state(api, Vehicle.BRAKE_PEDAL.STATES_V.PRESSED)
    set_gear_shifter_state(api, Vehicle.GEAR_SHIFTER.STATES_V.PARK)


@allure.step('Set battery state: {battery_state_v}')
def set_battery_state(api: VehicleApi, battery_state_v):
    api.pins.update_pin(Vehicle.BATTERY.PIN_ID, battery_state_v)


@allure.step('Set acceleration pedal state: {state_v}')
def set_acc_pedal_state(api: VehicleApi, state_v: float):
    api.pins.update_pin(Vehicle.ACC_PEDAL.PIN_ID, state_v)


@allure.step('Set brake pedal state: {state_v}')
def set_brake_pedal_state(api: VehicleApi, state_v):
    api.pins.update_pin(Vehicle.BRAKE_PEDAL.PIN_ID, state_v)


@allure.step('Set gear shifter state: {state_v}')
def set_gear_shifter_state(api: VehicleApi, state_v: tuple[float, float]):
    pins = api.pins.get_pins()
    pins.set_voltage(Vehicle.GEAR_SHIFTER.PIN_1_ID, state_v[0])
    pins.set_voltage(Vehicle.GEAR_SHIFTER.PIN_2_ID, state_v[1])
    api.pins.update_pins(pins)


@allure.step('Get battery state')
def get_battery_state(api: VehicleApi):
    return api.signals.get_signal(Vehicle.BATTERY.SIGNAL_ID).value


@allure.step('Get gear shifter state')
def get_gear_shifter_state(api: VehicleApi):
    return api.signals.get_signal(Vehicle.GEAR_SHIFTER.SIGNAL_ID).value


@allure.step('Get brake pedal state')
def get_brake_pedal_state(api: VehicleApi):
    return api.signals.get_signal(Vehicle.BRAKE_PEDAL.SIGNAL_ID).value


@allure.step('Get acceleration pedal state')
def get_acc_pedal_state(api: VehicleApi):
    return api.signals.get_signal(Vehicle.ACC_PEDAL.SIGNAL_ID).value


@allure.step('Get request torque state')
def get_req_torque_state(api: VehicleApi):
    return api.signals.get_signal(Vehicle.REQ_TORQUE.SIGNAL_ID).value

