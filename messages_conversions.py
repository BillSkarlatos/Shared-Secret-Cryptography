
def checkMessages():
    f=open("encrypted_messages.txt","r")
    if (len(f.readlines())==0):
        print("It looks like there are no messages to decrypt.")
        f.close()
        return 1
    f.close()
    return 0
