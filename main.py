# Importing our created files into main so that we can use the functions we created. 
from key_handling import *
from XOR_Gate import XOR
from messages_conversions import *
import sys

def option(choice):
    if (choice==1):
        if (checkMessages()==0):
            f=open("encrypted_messages.txt","r")
            keyIndex=0
            for msg in f.readlines():
                binaryMsg=toBinary(msg)
                newKeyLength=0
                # For easier handling, we convert the bit sequences to strings. This way, we will ba able to handle them like lists.
                for i in range(0,len(binaryMsg)):
                    binaryMsg[i]=str(binaryMsg[i])
                    newKeyLength+=len(binaryMsg[i])
                with open("secret_book.txt", 'r') as file:
                    for current_line_number, line in enumerate(file, start=0):
                        if current_line_number == keyIndex:
                            originalKey=''.join(line.strip().replace('[', '').replace(']', '').split(', '))
                            break
                print(originalKey)
                key=extendKey(originalKey,newKeyLength)
                print(key)
                keyIndex+=1
                c=0
                for i in range (0,len(binaryMsg)):
                    newBitSeq=''
                    for j in range(0,len(binaryMsg[i])):
                        newBitSeq+=str(XOR(int(binaryMsg[i][j]),int(key[c])))
                        c+=1
                    binaryMsg[i]=int(newBitSeq)
                result=toString(binaryMsg)
                print("Message ",keyIndex,":",result)


def main():
    choice=-1
    while (choice<0 or choice>4):
        sys.stdout.flush()
        choice=int(input("Please choose one of the following options: \nDecrypt all messages: 1\nEncrypt new message: 2\nGenerate new, or delete existing keys: 3\nYour choice: "))
    option(choice)
                



main()