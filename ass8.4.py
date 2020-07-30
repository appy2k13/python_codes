
fh = open('romeo.txt')
lst = list()
for line in fh:
    tlist = line.rstrip().split()
    #print (tlist)
    for word in tlist :
        #print(word)
        if word not in lst :
            lst.append(word)
lst.sort()
print(lst)
