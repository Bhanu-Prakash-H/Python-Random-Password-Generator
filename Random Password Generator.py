import random
u = 'ABCDEFGHIJKLMNOPQRSTVXYZ'
l = 'abcdefghijklmnopqrstvxyz'
s = '()[]{},.\/-'
all = u + l + s
length = 8
password = ''.join(random.sample(all,length))
print(password)