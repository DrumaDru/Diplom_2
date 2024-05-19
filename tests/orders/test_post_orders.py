import pytest
import json
import allure
import test_data
from helpers import Helpers

class TestOrders:

    @allure.title('Проверка создания заказа с передачей ингредиентов в тело запроса для авторизованного пользователя')
    @allure.description('Используем папаметризацию и создаем объект, который содержит элементы со значениями,'
                        'необходимыми для создания нового заказа.'
                        'Данный объект передаем в тело запроса и проверяем, что приходит статус ответа с кодом 200'
                        'и тело ответа содержит значение элемента name, идентификатор которого был передан в тело запроса.')
    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.bun, test_data.filling]},
    ])
    def test_authorized_order(self, payload):
        helpers = Helpers()
        response = helpers.authorized_order(payload)

        assert response.status_code == 200 and response.json()["name"] == "Бессмертный флюоресцентный бургер"

    @allure.title('Проверка создания заказа с передачей ингредиентов в тело запроса для неавторизованного пользователя')
    @allure.description('Используем папаметризацию и создаем объект, который содержит элементы со значениями,'
                        'необходимыми для создания нового заказа.'
                        'Данный объект передаем в тело запроса и проверяем, что приходит статус ответа с кодом 200'
                        'и тело ответа содержит значение элемента name, хеш которого был передан в тело запроса.')
    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.bun, test_data.filling]},
    ])
    def test_unauthorized_order(self, payload):
        helpers = Helpers()
        response = helpers.unauthorized_order(payload)

        assert response.status_code == 200 and response.json()["name"] == "Бессмертный флюоресцентный бургер"
    @allure.title('Проверка, получения статуса ответа с кодом 400, при передачи в тело запроса пустого объекта, который'
                  'должен содержать необходимые данные для создания нового заказа, для авторизованного пользователя.')
    @allure.description('Используем папаметризацию и создаем пустой объект.'
                        'Данный объект передаем в тело запроса и проверяем, что приходист статус ответа с кодом 401'
                        'и тело ответа содержит сообщение об ошибке.')
    @pytest.mark.parametrize("payload", [
        {"ingredients": []},
    ])
    def test_authorized_order_empty(self, payload):
        helpers = Helpers()

        response = helpers.authorized_order(payload)

        assert response.status_code == 400 and response.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверка, получения статуса ответа с кодом 500, при передачи в тело запроса хеша,'
                  'несуществующих ингредиентов.')
    @allure.description('Используем папаметризацию и создаем объект, элекмент которого содеражит, хеш несуществуюшего'
                        'ингредиента..'
                        'Данный объект передаем в тело запроса и проверяем, что приходит статус ответа с кодом 500.')
    @pytest.mark.parametrize("payload", [
        {"ingredients": [test_data.failed_hash]},
    ])
    def test_order_false_ingredient(self, payload):
        helpers = Helpers()

        response = helpers.authorized_order(payload)

        assert response.status_code == 500