import urllib.request, urllib.parse, urllib.error
fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
dect = dict()
for line in fh :
    words = line.decode().strip().split()
    #print(words)
    for word in words :
        dect[word] = dect.get(word, 0) + 1
ndl = list()
for k,v in dect.items() :
    #print(k,v)
    newt = (v,k)
    ndl.append(newt)
ndl = sorted(ndl, reverse = True)
lst = list()
for v, k in ndl:
    lst.append((k,v))
print(lst)
