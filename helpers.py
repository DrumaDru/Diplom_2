import requests
import json
import pytest
import allure
import test_data
import string
import random
import test_data

class Helpers:

    @allure.step('Создаем метод, который генерирует значения элементов словаря и возвращает его,'
                 'при вызове метода.')
    def generate_random_data_payload(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string


        # генерируем логин, пароль и имя курьера
        email_random_part = generate_random_string(10)
        email = email_random_part + "@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)


        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        # возвращаем payload
        return payload

    @allure.step('Создаем метод, который генерирует случайный хеш ингредиента и возвращает его значение.')
    def generate_random_hash(self):
        def generate_random_hash(length):
            characters = string.ascii_lowercase + string.digits
            random_hash = ''.join(random.choice(characters) for i in range(length))
            return random_hash

        # генерирум хеш ингредиента
        random_hash = generate_random_hash(24)

        return random_hash

    @allure.step('Создаем метод, который выполняет запрос на регистрацию пользователя с передачей в тело запроса,'
                 'сгенерированных значений элементов словаря payload и возвращает ответ, состоящий из статуса и тела овтета.')
    def registration_user(self, payload):
        response = requests.post(f"{test_data.curl}/api/auth/register", data=payload)
        return response

    @allure.step('Создаем метод, который выполняет запрос на авторизацию пользователя и возвращает ответ,'
                 'состоящий из статуса и тело ответа.')
    def login_user(self, payload):
        response = requests.post(f"{test_data.curl}/api/auth/login", data=payload)
        return response

    @allure.step('Создаем метод, который, вызывает метод на авторизацию пользователя и получает из тела ответа токен доступа.'
                 'Далее, метод, выполняет запрос на изменение данных пользователя и возвращает ответ, который содержит статус и'
                 'тело овтета.')
    def authorized_user_change(self, payload):
        token = self.login_user(test_data.login_payload).json()["accessToken"]
        headers = {
                "Authorization": f"{token}",
                 "Content-Type": "application/json"
            }
        payload = json.dumps(payload)

        response = requests.patch(f"{test_data.curl}/api/auth/user", headers=headers, data=payload)

        return response

    @allure.step('Создаем метод, который выполняет запрос на изменение данных для неавторизованного пользователя и'
                 'возвращает ответ, который содержит статус и тело овтета.')
    def unauthorized_user_change(self, payload):
        payload = json.dumps(payload)

        response = requests.patch(f"{test_data.curl}/api/auth/user", data=payload)

        return response

    @allure.step('Создаем метод, который вызывает метод на авторизацию пользователя и получает из тела ответа токен доступа.'
                 'Далее, метод выполняет запрос, на создание нового заказа и возвращает ответ,'
                 'который содержит статус и тело овтета.')
    def authorized_order(self, payload):
        token = self.login_user(test_data.login_payload).json()["accessToken"]
        headers = {
                "Authorization": f"{token}",
                 "Content-Type": "application/json"
            }
        payload = json.dumps(payload)
        response = requests.post(f"{test_data.curl}/api/orders", headers=headers, data=payload)

        return response

    @allure.step('Создаем метод, который выполняет запрос на создание нового заказа для неавторизованного пользователя'
                 'и возвращает ответ, который содержит статус и тело овтета.')
    def unauthorized_order(self, payload):
        payload = payload
        response = requests.post(f"{test_data.curl}/api/orders", data=payload)

        return response

    @allure.step('Создаем метод, который вызывает метод на авторизацию пользователя и получает из тела ответа токен доступа.'
                 'Далее метод, выполняет запрос на получение заказов для авторизованного пользователя и возвращает ответ,'
                 'который содержит статус и тело овтета.')
    def get_order_authorized_user(self):
        token = self.login_user(test_data.login_payload).json()["accessToken"]
        headers = {
                "Authorization": f"{token}",
                 "Content-Type": "application/json"
            }
        response = requests.get(f"{test_data.curl}/api/orders", headers=headers)

        return response


    @allure.step('Создаем метод, который выполняет запрос на получение заказов для неавторизованного пользователя и возвращает ответ,'
                 'который содержит статус и тело овтета.')
    def get_order_unauthorized_user(self):
        response = requests.get(f"{test_data.curl}/api/orders")

        return response