import allure
import pytest_check as check


@allure.step('Assert are equal: {current} value - {expected} value')
def equal(current, expected, parameter_name='testing parameter'):
    """
    Assertion method for checking equality of parameters.

    Args:
        current: Current value
        expected: Expected value
        parameter_name: Name of checking value

    Raises:
        AssertionError: in case if curren value is not equal with expected value
    """
    check.equal(current, expected,
                f"Current '{parameter_name}' with value: '{current}' is not equal with - Expected value: '{expected}'")
