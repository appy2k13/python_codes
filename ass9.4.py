name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        #print(words)
        sender[words[1]] = sender.get(words[1],0) + 1
#print(sender)
maxsend = None
maxsender = None
for k,v in sender.items() :
    if maxsend == None or v > maxsend :
        maxsender = k
        maxsend = v
print(maxsender, maxsend)
