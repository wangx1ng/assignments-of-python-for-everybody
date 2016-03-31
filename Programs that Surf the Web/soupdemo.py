# Scraping HTML Data with BeautifulSoup(Python 3.4.x)
from bs4 import *
from urllib.request import urlopen
import re

url = input("Enter url:")
html = urlopen(url).read()
soup = BeautifulSoup(html)

sum = 0
spans = soup("span")
for span in spans:
    span = str(span)
    nums = re.findall(">([0-9]+)<",span)
    for num in nums:
        sum = sum + int(num)

print (sum)
