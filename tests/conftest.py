"""
Config file for pytest tests in PL_Stat.
Author: Maciej Cisowski
"""
import pytest
from app.rest.rest_client import RestClient


def pytest_addoption(parser):
    """
    Add runtime options.
    :param parser: pytest fixture for parsing runtime options
    :return:
    """
    parser.addoption("--API_KEY", action="store", default="")


# FIXTURES


def api_key(request):
    return request.config.getoption('API_KEY')


@pytest.fixture(scope="session")
def rest(request) -> RestClient:
    return RestClient(ssl=True, api_key=api_key(request))
