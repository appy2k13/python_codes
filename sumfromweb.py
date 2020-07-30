import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_738328.html'
html = urllib.request.urlopen(url,context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sumval = 0
countval = 0
for tag in tags :
    sumval = sumval + int(tag.contents[0])
    countval = countval + 1;
print('Count :', countval)
print('Sum :', sumval)
