import pytest
import json
import test_data
from helpers import Helpers

class TestLogin:

    def test_login_user(self):
        helpers = Helpers()
        payload = test_data.login_payload

        response = helpers.login_user(payload)

        assert response.status_code == 200 and response.json()["user"]["email"] == payload["email"]

    @pytest.mark.parametrize("payload", [
        {"email": test_data.login_payload["email"], "password": "false_pass"},
        {"email": "false_email@yandex.ru", "password": test_data.login_payload["password"]}
    ])
    def test_incorrect_data(self, payload):
        helpers = Helpers()

        response = helpers.login_user(payload)

        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"
