# Extracting Data from JSON(Python 3.4.x)
import urllib.request
import json

url = input("Enter url:")
try:
    data = urllib.request.urlopen(url).read().decode("utf8")
    print(data)
except:
    print(url + " cannot be opened, now exit...")
    exit()
try:
    js = json.loads(data)
except Exception as e:
    print(e + " now exit...")
    exit()

sum = 0
for item in js["comments"]:
    sum = sum + item["count"]

print(sum)
