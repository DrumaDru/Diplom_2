import pytest
import json
import test_data
from helpers import Helpers


class TestUser:
    @pytest.mark.parametrize("payload", [
        {"password": test_data.login_payload["password"]},
        {"name": test_data.new_name}
    ])
    def test_authorized_user_change(self, payload):
        helpers = Helpers()

        response = helpers.authorized_user_change(payload)

        if "password" in payload:
            assert response.status_code == 200 and response.json()["success"] == True

        if "name" in payload:
            assert response.status_code == 200 and response.json()["user"]["name"] == payload["name"]

    @pytest.mark.parametrize("payload", [
        {"password": test_data.login_payload["password"]},
        {"name": test_data.new_name}
    ])
    def test_unauthorized_user_change(self, payload):
        helpers = Helpers()

        response = helpers.unauthorized_user_change(payload)

        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"