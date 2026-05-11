import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'https://quotes.toscrape.com/'

all_quotes = []

while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').text
        autor = quote.find('small', class_='author').text
        tags = [t.text for t in quote.find_all('a', class_='tag')]
        all_quotes.append({'text': text,
                    'author': autor,
                    'tags': tags})

    next = soup.find('li', class_='next')

    if next:
        url = 'https://quotes.toscrape.com/' + next.find('a')['href']
    else:
        break

authors = [q['author'] for q in all_quotes]
top3 = Counter(authors).most_common(3)
print(top3)