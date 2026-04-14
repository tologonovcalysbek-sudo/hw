# 1
import requests

# Эта библиотека нужна для получения данных с сайтов и API

response = requests.get("https://api.github.com")

print("Статус:", response.status_code)
print("Ответ:", response.text)


# 2
import requests

# Эта библиотека нужна для отправки данных на сервер,например: регистрация.

url = "https://httpbin.org/post"

user = {
    "name": "Kalys",
    "age": 19
}

response = requests.post(url, json=user)

print("Ответ сервера:", response.json())

