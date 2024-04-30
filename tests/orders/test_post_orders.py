import pytest
import json
import test_data
from helpers import Helpers

class TestOrders:

    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.bun, test_data.filling]},
    ])
    def test_authorized_order(self, payload):
        helpers = Helpers()

        response = helpers.authorized_order(payload)

        assert response.status_code == 200 and response.json()["name"] == "Бессмертный флюоресцентный бургер"

    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.bun, test_data.filling]},
    ])
    def test_unauthorized_order(self, payload):
        helpers = Helpers()

        response = helpers.unauthorized_order(payload)


        assert response.status_code == 200 and response.json()["name"] == "Бессмертный флюоресцентный бургер"

    @pytest.mark.parametrize("payload", [
        {"ingredients": []},
    ])
    def test_authorized_order_empty(self, payload):
        helpers = Helpers()

        response = helpers.authorized_order(payload)

        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.failed_hash]},
    ])
    def test_order_false_ingredient(self, payload):
        helpers = Helpers()

        response = helpers.authorized_order(payload)

        assert response.status_code == 500