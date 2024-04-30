import pytest
import json
import test_data
from helpers import Helpers

class TestOrdersUser:
    def test_get_order_authorized_user(self):
        helpers = Helpers()

        response = helpers.get_order_authorized_user()

        assert response.status_code == 200 and response.json()["total"] > 0

    def test_get_order_unauthorized_user(self):
        helpers = Helpers()

        response = helpers.get_order_unauthorized_user()

        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"