import urllib.request
import bs4

url = "https://naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

print(bs_obj)