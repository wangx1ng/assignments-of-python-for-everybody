# Using the GeoJSON API(Python 3.4.x)
import json
import urllib.request
import urllib.parse

location = input("Enter location:")
apiurl = "http://python-data.dr-chuck.net/geojson?"
serviceurl = apiurl + urllib.parse.urlencode({"sensor":"false", "address":location})
try:
    data = urllib.request.urlopen(serviceurl).read().decode("utf8")
except Exception as e:
    print(e)
    exit()
try:
    js = json.loads(data)
except Exception as e:
    print(e)
    exit()

id = js["results"][0]["place_id"]
print(id)
