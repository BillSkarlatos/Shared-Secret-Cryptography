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
                key=extendKey(originalKey,newKeyLength)
                keyIndex+=1
                c=0
                for i in range (0,len(binaryMsg)):
                    newBitSeq=''
                    for j in range(0,len(binaryMsg[i])):
                        newBitSeq+=str(XOR(int(binaryMsg[i][j]),int(key[c])))
                        c+=1
                    binaryMsg[i]=int(newBitSeq)
                message=toString(binaryMsg)
                print("Message ",keyIndex,":",message)
            f.close()   
        else:
            newChoice=int(input("No messsages and keys found, would you like to generate keys?\n Press [1 for Yes] or anything other for Exit. "))
            if (newChoice==1):
                option(3)
            else:
                option(4)
    elif (choice==3):
        generateKeys()
        newChoice=int(input("Would you like to encrypt a new message now?\nPress [1 for Yes] or anything else for Exit. "))
        if (newChoice==1):
            option(2)
        else:
            option(4)
    elif(choice==4):
        print("Thanks for trying out my Project!")
        return
    else: #choice==2
        
    
            

def main():
    choice=-1
    while (choice<0 or choice>5):
        sys.stdout.flush()
        choice=int(input("Please choose one of the following options: \nDecrypt all messages: 1\nEncrypt new message: 2\nGenerate new, or delete existing keys: 3\nExit Program: 4\nYour choice: "))
    option(choice)
                



main()