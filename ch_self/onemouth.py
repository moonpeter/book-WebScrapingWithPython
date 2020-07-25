import urllib.request

url = "https://naver.com"
html = urllib.request.urlopen(url)

print(html.read())