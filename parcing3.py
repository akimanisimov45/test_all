import requests
import time

def safe_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for attempt in range(3):
        try:
            r = requests.get(url, headers=headers)
            return r.text
        except requests.exceptions.ConnectionError:
            print(f'Попытка {attempt + 1} провалилась')
            time.sleep(1)

    return None

result = safe_url('https://quotes.toscrape.com')
print(f'Успех: {len(result)},')