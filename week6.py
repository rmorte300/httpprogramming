#1
import http.client


connection = http.client.HTTPSConnection("www.python.org")
connection.request("GET","/")

    
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)
if response.status == 200:
    data = response.read()
    print(data)


#2

import http.client


connection = http.client.HTTPConnection("www.python.org")
connection.request("GET","/")

response = connection.getresponse()

print(type(response))
print(response.status, response.reason, response.headers)
if response.status == 200:
    data = response.read()
    print(data)

#3
import urllib.request

connection = "https://www.python.org/"
response = urllib.request.urlopen(connection)
html = response.read()[:600]
print(html)


#4

import urllib.request

connection = "https://www.python.org/"
response = urllib.request.urlopen(connection)
html = response.read()[:600]
print(html.decode('utf-8'))

#5
from urllib.request import urlopen

link = urlopen('https://www.google.com')
print(link)
print(link.readline())

