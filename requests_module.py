import requests
# Сервис теста API - https://reqres.in/

# Пример GET-запроса (получение информации о пользователе)
link = "https://reqres.in/api/users/2"
r_get = requests.get(link)
print(r_get.json())

# Пример POST-запроса 1 (создание пользователя)
link_2 = "https://reqres.in/api/users"
data = {"name": "Artyom", "job": "Tester"}
r_post = requests.post(link_2, data=data)
print(r_post.json())

dic_response = r_post.json()
print(type(dic_response))
print(dic_response.get("createdAt"))



# Пример POST-запроса 2 (авторизация и получение токена)
link_3 = "https://reqres.in/api/login"
data_2 = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
r_post_2 = requests.post(link_3, data=data_2)
print(r_post_2.json())


# Запись тела ответа в JSON
ssilka = "https://reqres.in/api/unknown"
r = requests.get(ssilka)
with open("files/response.json", "w") as response:
    response.write(r.text)