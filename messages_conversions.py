import math
from XOR_Gate import XOR

def checkMessages():
    f=open("encrypted_messages.txt","r")
    if (len(f.readlines())==0):
        print("It looks like there are no messages to decrypt.")
        f.close()
        return 1
    f.close()
    return 0

# String to binary conversion.
def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    for i in range(0,len(m)):
        m[i]=str(m[i])
    return m

# Binary to String Conversion.
def toString(a):
    l=[]
    m=""
    for i in a:
        b=0
        c=0
        k=int(math.log10(i))+1
        for j in range(k):
            b=((i%10)*(2**j))   
            i=i//10
            c=c+b
        l.append(c)
    for x in l:
        m=m+chr(x)
    return m

# Applying XOR for every bit of the key and the message. The arguments and the return value is a list of binary values.
def convert(message,key):
    result=[]
    for i in range(0,len(message)):
        result.append(XOR(message[i],key[i]))
    return result