"""
Config file for pytest tests in PL_Stat.
Author: Maciej Cisowski
"""
import pytest
from app.rest.rest_client import RestClient
from app.helpers.environment import get_api_key


# FIXTURES

@pytest.fixture(scope="session")
def rest() -> RestClient:
    return RestClient(ssl=True, api_key=get_api_key())
