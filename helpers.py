import requests
import json
import pytest
import allure
import test_data
import string
import random

class Helpers:

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


    def registration_user(self, payload):
        response = requests.post(f"{test_data.curl}/api/auth/register", data=payload)
        return response
