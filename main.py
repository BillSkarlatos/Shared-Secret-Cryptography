# Importing our created files into main so that we can use the functions we created. 
from key_handling import *
from XOR_Gate import XOR
import sys

def main():
    choice=-1
    while (0>choice or choice>4):
        sys.stdout.flush()
        choice=int(input("Please choose one of the following options: \nDecrypt all messages: 1\nEncrypt new message: 2\nGenerate new, or delete existing keys: 3\nYour choice: "))
        print(choice)

main()