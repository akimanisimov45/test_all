import requests
from collections import Counter

url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
posts = r.json()

users = [t['userId'] for t in posts]
topchik = Counter(users).most_common(1)
user3 = [t['title'] for t in posts if t['userId'] == 3]

print(topchik)