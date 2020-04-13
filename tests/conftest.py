"""
Config file for pytest tests in PL_Stat.
Author: Maciej Cisowski
"""
import pytest
from app.rest.rest_client import RestClient
from app.helpers.environment import get_api_key


def pytest_addoption(parser):
    """
    Add runtime options.
    :param parser: pytest fixture for parsing runtime options
    :return:
    """
    parser.addoption("--API_KEY", action="store", default="")


# FIXTURES

@pytest.fixture(scope="session")
def rest() -> RestClient:
    return RestClient(ssl=True, api_key=get_api_key())
