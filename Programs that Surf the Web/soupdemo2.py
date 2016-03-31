# Following Links in HTML Using BeautifulSoup(Python 3.4.x)
from bs4 import *
from urllib.request import urlopen

while True:
    url = input("Input the url:")
    if url == "quit":
        exit()
    try:
        urlopen(url)
    except:
        print("Cannot reach url: " + url + ", restart...")
        continue
    pos = input("Input the position in number:")
    try:
        position = int(pos)
    except:
        print("Not a number, restart...")
        continue
    tim = input("Input the times in number:")
    try:
        times = int(tim)
        break
    except:
        print("Not a number, restart...")
        continue

for i in range(times):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    urls = list()
    tags = soup("a")
    for tag in tags:
        urls.append(tag.get("href", None))
    url = urls[position -1]
    print(url)
