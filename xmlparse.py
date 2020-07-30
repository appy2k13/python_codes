import urllib.request as UR, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL : ")
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_738330.xml'
print(url)
xmldoc = UR.urlopen(url,context = ctx).read().decode()
print(xmldoc)
tree = ET.fromstring(xmldoc)
print(tree)
#counts = tree.findall('.//count')
sum = 0
c = 0
for line in xmldoc:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    print(type(num))
    #print (num)
    if  len(num) < 1:
        continue
    else :
        print(num)
        for val in num:
            c = c + 1
            sum = (sum + int(val))
print('Count: ',c, '\nSum: ', sum)
