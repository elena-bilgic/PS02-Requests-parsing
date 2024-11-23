# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId" : 1
}
response = requests.get(url, params=params)

print(f"Status code: {response.status_code}")
response_json = response.json()
pprint.pprint(response_json)