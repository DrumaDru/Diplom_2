import pytest
import json
from helpers import Helpers

class TestRegister:

    def test_register_new_user(self):
        helpers = Helpers()

        payload = helpers.generate_random_data_payload()

        responce = helpers.registration_user(payload)

        assert responce.status_code == 200 and responce.json()["user"]["email"] == payload["email"]




