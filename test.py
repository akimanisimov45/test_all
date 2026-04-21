import requests

request = requests.get('https://httpbin.org/get')
print(request.status_code)
print(request.headers)
print(request.json())

try:
    request1 = requests.get('https://notwork.xuy')
except requests.exceptions.ConnectionError:
    print('Данный сайт недоступен')