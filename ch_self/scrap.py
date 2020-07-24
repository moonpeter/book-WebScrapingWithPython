import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/digital/')
soup = BeautifulSoup(res.content, 'html.parser')

# link_title = soup.find_all('a', class_='link_txt')
link_title = soup.find_all('a', attrs={'class': 'link_txt', 'data-tiara-type': 'harmony'})

for num in range(len(link_title)):
    print(link_title[num].get_text().strip())
