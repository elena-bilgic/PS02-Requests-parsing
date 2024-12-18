# Задание 1: Получение данных. Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

url = "https://api.github.com"

params = {
    "q" : "html"
}

response = requests.get(url, params=params)
print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)
