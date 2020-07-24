import requests
from bs4 import BeautifulSoup

URL_TOTAL_LIST = 'https://comic.naver.com/webtoon/weekday.nhn'

response = requests.get(URL_TOTAL_LIST)
soup = BeautifulSoup(response.text, 'html.parser')
class_title_a_list = soup.select('a.title')

title_list = []

for a in class_title_a_list:
    a_href = a.get('href') # a['href']
    a_text = a.get_text()
    result = f'{a_text} (https://comic.naver.com/{a_href})'
    title_list.append(result)

print('\n'.join(title_list))
