"""
Test for the general rest client used by the PL_Stat app.
Author: Maciej Cisowski
"""
from assertpy import assert_that


class TestRestClient(object):
    resource_path = "data/by-variable/3643?format=json&year=2000&year=2010"

    def test_rest_client_returns_200_status_code(self, rest):
        assert_that(rest
                    .get(resource_path=self.resource_path)
                    .status_code)\
            .is_equal_to(200)

    def test_rest_client_returns_expected_json_keys(self, rest):
        expected_keys = ["aggregateId", "lastUpdate", "links",
                         "measureUnitId", "results", "totalRecords",
                         "variableId"]
        assert_that(rest
                    .get(resource_path=self.resource_path)
                    .json().keys()).contains(*expected_keys)
