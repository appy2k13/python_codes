import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter URL : ")
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/known_by_Dhani.html'
count = input('Enter Count')
if count == '' :
    count = 7
else :
    count = int(count)
pos = input('Enter position')
if pos == '' :
    pos = 17
else :
    pos = int(pos) - 1
i = count
print(url)
print(count)
print(pos)
while(i) :
    html = urllib.request.urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(html[0])
    tags = soup('a')
    url = tags[pos].get('href', None)
    sval = tags[pos].contents[0]
    print(url)
    print(sval, '\n')
    i = i - 1
print(sval)
