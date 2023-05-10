import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top'
page = requests.get(url)

# 1. Using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

tag = soup.find('div', class_=re.compile(r'by+'))
info = tag.text
# print(info)


# 2. Using Regex
info = re.findall(r'<title>(.*?)</title>', page.text)
print(info)