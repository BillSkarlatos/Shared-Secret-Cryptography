from key_handling import *
from messages_conversions import *
from XOR_Gate import *

a=toBinary("Hello World")
for i in range(0,len(a)):
    a[i]=str(a[i])
print(a)
for i in range(0,len(a)):
    a[i]=int(a[i])
a=toString(a)
print(a)