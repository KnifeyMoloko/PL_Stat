"""
Tests for helper functions for the PL_Stat app.
Author: Maciej Cisowkski
"""
import pytest
from assertpy import assert_that
from app.helpers.environment import get_env_vars, get_api_key


class TestEnvironment(object):
    @pytest.fixture(scope='function')
    def set_up_env_vars(self, monkeypatch):
        monkeypatch.setenv("API_KEY", "randomcharactershere")

    def test_get_env_vars_returns_dict(self):
        assert_that(get_env_vars()).is_type_of(dict)

    def test_get_api_key_return_string(self, set_up_env_vars):
        assert_that(get_api_key()).is_type_of(str)
