import requests
import bs4


def webtoon(url):
    results = requests.get(url=url)
    bs_obj = bs4.BeautifulSoup(results.content, "html.parser")

    tables = bs_obj.findAll("td", {"class": "title"})
    hrefs = [td.find("a")["href"] for td in tables]

    titles = [td.find("a") for td in tables]

    view_list = bs_obj.find('table', {'class': "viewList"})
    img_in_view_list = view_list.find_all('img')
    imgs = []
    for j in range(len(img_in_view_list)):
        imgs.append(((img_in_view_list)[j])['src'])

    for i in range(len(hrefs)):
        print('---------------------------------------------------')
        print('title : ' + titles[i].text)
        print('links : ' + 'https://comic.naver.com' + hrefs[i])
        print('image : ' + imgs[i])
        i += 1


webtoon('https://comic.naver.com/webtoon/list.nhn?titleId=602910&weekday=mon')
webtoon('https://comic.naver.com/webtoon/list.nhn?titleId=602910&weekday=mon&page=2')
