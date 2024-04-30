import pytest
import json

import test_data
from helpers import Helpers

class TestRegister:

    def test_register_new_user(self):
        helpers = Helpers()
        payload = helpers.generate_random_data_payload()

        responce = helpers.registration_user(payload)

        assert responce.status_code == 200 and responce.json()["user"]["email"] == payload["email"]



    def test_duplicate_user(self):
        helpers = Helpers()
        payload = helpers.generate_random_data_payload()
        helpers.registration_user(payload)

        responce = helpers.registration_user(payload)

        assert responce.status_code == 403 and responce.json()["message"] == "User already exists"

    @pytest.mark.parametrize("payload", [
        {"password": test_data.password, "name": test_data.name},
        {"email": test_data.email, "name": test_data.name},
        {"email": test_data.email, "password": 'test_data.password'}

    ])
    def test_not_all_fields(self, payload):
        helpers = Helpers()


        responce = helpers.registration_user(payload)

        assert responce.status_code == 403 and responce.json()["message"] == "Email, password and name are required fields"







