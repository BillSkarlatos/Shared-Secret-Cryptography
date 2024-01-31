# Importing our created files into main so that we can use the functions we created. 
from key_handling import *
from XOR_Gate import xor_gate
from messages_conversions import *
import sys
import ast

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def option(choice):
    if (choice==1):
        if (checkMessages()==0):
            messages = read_file("encrypted_messages.txt")
            keys = read_file("secret_book.txt")
            # Perform XOR decryption
            for message, key in zip(messages, keys):
                decoded_message = xor_gate(message, key)
                print(decoded_message)
        else:
            newChoice=int(input("No messsages and keys found, would you like to encode new messages?\n Press [1 for Yes] or anything other for Exit. "))
            if (newChoice==1):
                option(2)
            else:
                option(4)
    elif (choice==3):
        clearKeys()
        print("Clean Slate!")
        newChoice=int(input("Would you like to encrypt a new message now?\nPress [1 for Yes] or anything else for Exit. "))
        if (newChoice==1):
            option(2)
        else:
            option(4)
    elif(choice==4):
        print("Thanks for trying out my Project!")
        return
    else: #choice==2
        message=input("Give me the message you want to encrypt ")
        key=generate_key(len(message))
        encoded_message = xor_gate(message, key)
        f=open("encrypted_messages.txt","a")
        g=open("secret_book.txt","a")
        f.write(encoded_message)
        f.write("\n")
        g.write(key)
        g.write("\n")
        f.close()
        g.close
        print("Result: ",encoded_message," has been saved")
        newChoice=int(input("Would you like to encrypt a new message?\nPress [1 for Yes] or anything else for Exit. "))
        if (newChoice==1):
            option(2)
        else:
            option(4)

    
            

def main():
    choice=-1
    while (choice<0 or choice>5):
        sys.stdout.flush()
        choice=int(input("Please choose one of the following options: \nDecrypt all messages: 1\nEncrypt new message: 2\nClear messages and keys: 3\nExit Program: 4\nYour choice: "))
    option(choice)
                



main()