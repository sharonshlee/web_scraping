import requests
from bs4 import BeautifulSoup

content = requests.get('https://github.com/search?q=chatgpt', timeout=5).text

soup = BeautifulSoup(content, 'html.parser')
repos = soup.find_all('li', class_='repo-list-item')

for repo in repos:
    for link in repo.find_all('a', class_='v-align-middle'):
        print(f"https://github.com/{link['href']}")
