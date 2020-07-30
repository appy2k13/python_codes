import re

fname = input("Enter file name")
hand = open(fname,'r')

sum = 0
for line in hand :
    line = line.rstrip()
    numlist = re.findall('[0-9]+', line)
    for val in numlist :
        sum = sum + int(val)
print(sum)
