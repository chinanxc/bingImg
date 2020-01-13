import requests
from bs4 import BeautifulSoup

urlbase = "https://bing.ioliu.cn/"
maxpage = 117

for i in range(maxpage):
    url = urlbase + "?p=" + str(i)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',class_='item')
    for item in items:
        imgurl = item.find('img')['src']
        print(imgurl)

print('ok')