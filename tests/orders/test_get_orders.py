import pytest
import json
import test_data
import allure
from helpers import Helpers

class TestOrdersUser:
    @allure.title('Проверка получения заказов авторизованного пользователя.')
    @allure.description('С помощью вспомогательного метода, выполняем запрос на авторизацию существуюшего пользователя'
                        'и получаем токен из тела ответа.'
                        'Полученный токен передаем в раздел Headers, запроса на получение заказов пользователя'
                        'и проверяем, что приходит статус ответа с кодом 200 и тело запроса содеражит значение элемента'
                        'total больше нуля.')
    def test_get_order_authorized_user(self):
        helpers = Helpers()

        response = helpers.get_order_authorized_user()

        assert response.status_code == 200 and response.json()["total"] > 0
    @allure.title('Проверка статуса ответа с кодом 401 при выполнении запоса на получение заказов'
                  'неавторизованного пользователя.')
    @allure.description('Выполняем запрос на получение заказов для неваторизованного пользователя и проверяем,'
                        'что приходит статус ответа с кодом 401 и тело ответа содержит сообщение об ошибке')
    def test_get_order_unauthorized_user(self):
        helpers = Helpers()

        response = helpers.get_order_unauthorized_user()

        assert response.status_code == 401 and response.json()["message"] == "You should be authorised"