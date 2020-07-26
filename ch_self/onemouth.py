import urllib.request

import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
div = bs_obj.find("div", {"class": "main_component droppable", "id": "section_politics"})
strong = div.findAll("strong")

for s_tag in strong:
    print(s_tag.text)
    print(s_tag.text)
    print(s_tag.text)
    print(s_tag.text)
