# This will generate 5-bit random keys to only be used once.
import random

def generateKeys():
    Num=int(input("How many new keys do you want to generate? (type a negative Number to erase all the previous keys) "))
    while (Num<0):
        # Informing the User about how many keys will be deleted. Since every key takes up one line of the .txt file, 
        # we read the file and count the lines, the result of the count is the number of keys in the file.
        f=open("secret_book.txt", "r")
        x = len(f.readlines())
        print("Deleting ",x," keys ...")
        f.close()

        # We open and close the file using the "write" method, which overwrites the keys with nothing.  
        open("secret_book.txt", "w").close()
        # Since deleting the keys will make the encrypted messages unreadable, we delete them as well
        open("encrypted_messages.txt", "w").close()
        
        # These lines are both for generating new keys after deletion and for error prevention.
        print("--- Please, now select a number over 0 ---")
        Num=int(input("How many new keys do you want to generate? "))

    f = open("secret_book.txt", "a")
    for i in range(0,Num):
        key=[]
        for j in range(0,5):
            bit_value=random.randrange(0,2)
            key.append(bit_value)
        print("New key: ",str(key))
        f.write(str(key))
        f.write("\n")
    f.close()

def checkIfEmpty():
    f=open("secret_book.txt", "r")
    if (len(f.readlines())==0):
        print("It looks like there are no available keys at the moment, you have to generate more before proceeding")
        f.close()
        generateKeys()
    else: 
        f.close()

def extendKey(originalKey, length):
    # This is a deviation from the original algorithmic logic because when you have capped key length,
    # the maximum amount of keys that you will be able to produce is 2^{max_length}, but, since theoretically no one
    # has access to the keys or the information about them, it should still be impossible to establish the extended pattern.
    counter=0
    extendedKey=[]
    for i in range(0,length):
        extendedKey.append(originalKey[counter])
        if (counter+1>=len(originalKey)):
            counter=0
        else:
            counter+=1
    return extendedKey

    