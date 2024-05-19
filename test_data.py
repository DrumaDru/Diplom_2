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


#Бессмертный флюоресцентный бургер
bun = "61c0c5a71d1f82001bdaaa6d" #Флюоресцентная булка R2-D3
filling = "61c0c5a71d1f82001bdaaa6f" #Мясо бессмертных моллюсков Protostomia

failed_hash = helpers.generate_random_hash()