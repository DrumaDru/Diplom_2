import random
from helpers import Helpers

curl = "https://stellarburgers.nomoreparties.site"

email = "test_user@yandex.ru"
password = "123456"
name = "User"

login_payload = {
"email": "test-user003@yandex.ru",
"password": "1234567"
}

helpers = Helpers()
new_name = helpers.generate_random_data_payload()["name"]

