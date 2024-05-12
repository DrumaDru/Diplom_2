import pytest
import allure
import json
import test_data
from helpers import Helpers


class TestUser:
    @allure.title('Проверка изменения данных авторизованного пользователя')
    @allure.description('Применяем параметризацию, в котором создаем объект, который содержит элементы'
                        'со значениями пароля и почты, для изменения данных авторизованного пользователя.'
                        'Передаем объекты в тело запроса на изменение данных.'
                        'Проверяем, что приходит стауст ответа с кодом 200 и тело ответа содержит значение'
                        'True в элементе success, при изменении пароля и содержит имя, переданное в тело запроса')
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

    @allure.title('Проверка получения статус ответа с кодом 401 при передачи в тело запроса данных для изменения,'
                  'для неавторизованного пользователя')
    @allure.description('Применяем параметризацию, в котором создаем объект, который содержит элементы'
                        'со значениями пароля и почты, для изменения данных неавторизованного пользователя.'
                        'Передаем объекты в тело запроса на изменение данных.'
                        'Проверяем, что приходит стауст ответа с кодом 401 и тело ответа содержит сообщеие об ошибке.')
    @pytest.mark.parametrize("payload", [
        {"password": test_data.login_payload["password"]},
        {"name": test_data.new_name}
    ])
    def test_unauthorized_user_change(self, payload):
        helpers = Helpers()

        response = helpers.unauthorized_user_change(payload)

        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"