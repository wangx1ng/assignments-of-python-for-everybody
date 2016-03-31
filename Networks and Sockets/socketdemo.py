# Understanding the Request / Response Cycle(Python 2.7.x)
import socket as sc

# Connect to host
mysock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
host = raw_input("Enter the host:")
try:
    mysock.connect((host, 80))
except:
    print "Host cannot be connected, now exit..."
    exit()
print "Connected to",host

# Get data
while True:
    url = raw_input("Enter the url:")
    try:
        mysock.send("GET " + url + " HTTP/1.0\n\n")
        break
    except:
        print "Wrong url, enter again..."
        continue

while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print data

mysock.close()
