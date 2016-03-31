# Extracting Data from XML(Python 3.4.x)
import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter url:")
try:
    data = urllib.request.urlopen(url).read()
except:
    print("URL " + url + " cannot be opened, now exit...")
    exit()

tree = ET.fromstring(data)
counts = tree.findall(".//count")
print("There are " + str(len(counts)) + " counts.")
# print(counts)

sum = 0
for count in counts:
    num = count.text
    sum = sum + int(num)
print(sum)
