"""
Config file for pytest tests in PL_Stat.
Author: Maciej Cisowski
"""
import pytest
from app.rest.PLStatClient import PLStatClient
from app.helpers.environment import get_api_key


# FIXTURES

@pytest.fixture(scope="session")
def rest() -> PLStatClient:
    return PLStatClient(ssl=True, api_key=get_api_key())
