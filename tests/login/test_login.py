import pytest
import allure
import json
import test_data
from helpers import Helpers

class TestLogin:

    @allure.title('Проверка авторизации существующего пользователя.')
    @allure.description('В поле запроса на авторизацию передаем объект, содержащий данные, существующего пользователя.'
                        'Проверяем, что приходит стаус ответа с кодом 200 и тело ответа содержит почту, такую же,'
                        'которая была передана в тело запроса.')
    def test_login_user(self):
        helpers = Helpers()
        payload = test_data.login_payload

        response = helpers.login_user(payload)

        assert response.status_code == 200 and response.json()["user"]["email"] == payload["email"]

    @allure.title('Проверка авторизации с неверным логином и паролем')
    @allure.description('Применяем параметризацию, в котором создаем объект, который содержит элементы'
                        'с невалидными значениями почты и пароля.'
                        'Проверяем, что при передачи в тело запроса объекта с невалидными значениями почты и пароля,'
                        'приходит статус ответа с кодом 401 и тело ответа содержит сообщение об ошибке. ')
    @pytest.mark.parametrize("payload", [
        {"email": test_data.login_payload["email"], "password": "false_pass"},
        {"email": "false_email@yandex.ru", "password": test_data.login_payload["password"]}
    ])
    def test_incorrect_data(self, payload):
        helpers = Helpers()

        response = helpers.login_user(payload)

        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect"
