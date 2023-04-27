import re
import requests
from bs4 import BeautifulSoup

content = requests.get('https://www.rottentomatoes.com/m/spiderman', timeout=5).text

soup = BeautifulSoup(content, features="html.parser")

info_title = soup.find("h2", {'data-qa': "movie-info-section-title"}).text.strip()
print(info_title)
info_summary = soup.find('p', {'data-qa': 'movie-info-synopsis'}).text.strip()
print(info_summary)
print()


info_dict = {}
for info in soup.find_all("li", class_="info-item"):
    info_dict[info.find('b', class_='info-item-label').text.strip()] = \
        re.sub(r'\s{2,}', ' ', info.find('span', class_='info-item-value').text.strip())

print("\n".join([f"{key} {value}" for key, value in info_dict.items()]))