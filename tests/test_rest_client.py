"""
Test for the general rest client used by the PL_Stat app.
Author: Maciej Cisowski
"""
import pytest
from assertpy import assert_that
from app.rest.rest_client import RestClient


class TestRestClient(object):
    def test_rest_client_returns_200_status_code(self, rest):
        assert_that(
            rest.get(
                resource_path="data/by-variable/3643"
                              "?format=json&year=2000&year=2010")
                .status_code)\
            .is_equal_to(200)
