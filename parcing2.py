import requests

# Без заголовка — как бот
r1 = requests.get('https://quotes.toscrape.com')
print('Без заголовка:', r1.status_code)

# С заголовком — притворяемся браузером
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
r2 = requests.get('https://quotes.toscrape.com', headers=headers)
print('С заголовком:', r2.status_code)