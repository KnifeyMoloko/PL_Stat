"""
Test for the general rest client used by the PL_Stat app.
Author: Maciej Cisowski
"""
import pytest
from assertpy import assert_that
from app.rest.rest_client import RestClient
from app.helpers.environment import get_api_key


class TestRestClient:
    @pytest.fixture
    def client(self) -> RestClient:
        client = RestClient(ssl=True,
                            host="bdl.stat.gov.pl",
                            endpoint="/api/v1/",
                            api_key=get_api_key())
        return client

    resource_path = "data/by-variable/3643?format=json&year=2000&year=2010"

    def test_rest_client_returns_200_status_code(self, client):
        assert_that(client
                    .get(resource_path=self.resource_path)
                    .status_code)\
            .is_equal_to(200)

    def test_rest_client_returns_expected_json_keys(self, client):
        expected_keys = ["aggregateId", "lastUpdate", "links",
                         "measureUnitId", "results", "totalRecords",
                         "variableId"]
        assert_that(client
                    .get(resource_path=self.resource_path)
                    .json().keys()).contains(*expected_keys)
