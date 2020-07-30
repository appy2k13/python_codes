name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        time = words[5].split(':')
        hour[time[0]] = hour.get(time[0],0) + 1
for k,v in sorted(hour.items()) :
    print(k,v)
