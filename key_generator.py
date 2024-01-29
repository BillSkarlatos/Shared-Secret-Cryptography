# This will generate 5-bit ranodm keys to only be used once
import random

Num=int(input("How many new keys do you want to generate? "))
while (Num<=0):
    print("--- Please select a number over 0! ---")
    Num=int(input("How many new keys do you want to generate? "))
f = open("secret_book.txt", "a")
for i in range(0,Num):
    key=[]
    for j in range(0,5):
        bit_value=random.randrange(0,2)
        key.append(bit_value)
    print("New key: ",str(key))
    f.write(str(key))
f.close()