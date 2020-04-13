"""
Test for listing general categories used by the PL_Stat app.
Author: Maciej Cisowski
"""
from assertpy import assert_that, soft_assertions
from http import HTTPStatus


class TestGeneralLists:
    def test_get_levels_list_returns_ok(self, rest):
        response = rest.get_levels()
        expected_status = HTTPStatus.OK
        assert_that(response.status_code).is_equal_to(expected_status)

    def test_get_levels_list_has_expected_items(self, rest):
        response = rest.get_levels().json()
        expected_items = ["totalRecords", "results"]
        assert_that(response).contains(*expected_items)

    def test_get_levels_list_has_expected_subitems(self, rest):
        response = rest.get_levels().json()
        expected_subitems = ["id", "name"]
        with soft_assertions():
            for item in response.get('results'):
                assert_that(item).contains(*expected_subitems)
