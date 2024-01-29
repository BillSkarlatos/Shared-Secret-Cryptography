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