import re
t = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('\S+?@\S+', t)
print(y)
