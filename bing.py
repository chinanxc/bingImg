import requests
import json
import time

path = "/Users/neeck/Downloads/bing/"
uribase = "https://cn.bing.com"
url = uribase +"/HPImageArchive.aspx?format=js&n=1&idx=0"
re = requests.get(url)
# time.sleep(3)
data = json.loads(re.text)
cop = data["images"][0]["copyright"]
imgurl = uribase + data["images"][0]["url"]
filename = data["images"][0]["enddate"] + ".jpg"

print(cop)
print(imgurl)
r = requests.get(imgurl)

with open(path + filename,"wb") as f:
    f.write(r.content)
print("图片  " + filename + " Downing Good!")
