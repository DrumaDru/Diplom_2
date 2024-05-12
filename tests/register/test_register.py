import pytest
import json
import allure
import test_data
from helpers import Helpers

class TestRegister:

    @allure.title('Проверка создания уникального пользователя.')
    @allure.description('С помощью вспомогательного метода, генерируем рандомные значения элементов объекта с данным регистрации и'
                        'передаем их в тело запроса на регистрациию нового пользователя.'
                        'Проверяем, что приходит статус ответа с кодом 200 и тело запроса содержит значение почты,'
                        'которое передавалось в тело запроса на регистарцию нового пользователя.')
    def test_register_new_user(self):
        helpers = Helpers()
        payload = helpers.generate_random_data_payload()

        response = helpers.registration_user(payload)

        assert response.status_code == 200 and response.json()["user"]["email"] == payload["email"]


    @allure.title('Проверка статуса ответа с кодом ошибки 403, при попытки зарегистрировать нового пользователя,'
                  'с почтой существующего пользователя.')
    @allure.description('С помощью вспомогательного метода, генерируем рандомные значения элементов объекта с данным регистрации и'
                        'сохраняем данные в переменную. '
                        'Переменную с данным для регистрации передаем в тело запроса на регистрациию нового пользователя.'
                        'Затем те же данные, повторно передаем в регистрацию нового пользователя.'
                        'Проверем, что приходит статус ответа с кодом 403 и тело запроса содержит сообщение об ошибке.')
    def test_duplicate_user(self):
        helpers = Helpers()
        payload = helpers.generate_random_data_payload()
        helpers.registration_user(payload)

        response = helpers.registration_user(payload)

        assert response.status_code == 403 and response.json()["message"] == "User already exists"

    @allure.title('Проверка статуса ответа с кодом ошибки 403, при передаче в тело запроса на регистрацию,'
                  'не все обязательные поля.')
    @allure.description('Применяем параметрезацию, в которой создаем объект, который содержит не все обязательные, элементы'
                        'для запроса регистрации.'
                        'Проверяем, что приходит статус ответа с кодом 403 и тело ответа содержит сообщение об ошибке.')
    @pytest.mark.parametrize("payload", [
        {"password": test_data.password, "name": test_data.name},
        {"email": test_data.email, "name": test_data.name},
        {"email": test_data.email, "password": 'test_data.password'}

    ])
    def test_not_all_fields(self, payload):
        helpers = Helpers()


        response = helpers.registration_user(payload)

        assert response.status_code == 403 and response.json()["message"] == "Email, password and name are required fields"







