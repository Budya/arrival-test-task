import pytest

from project.classes.api.vehicle_api import VehicleApi
from project.config import BASE_URL
from project.steps import steps


@pytest.fixture
def api(request) -> VehicleApi:
    url = request.config.getoption("--base_url")
    return VehicleApi(url)


@pytest.fixture(autouse=True)
def reset_system_state(api: VehicleApi):
    steps.reset_system_state(api)


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default=BASE_URL)
