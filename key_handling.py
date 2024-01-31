# This will generate 5-bit random keys to only be used once.
import secrets
import string

def generate_key(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def clearKeys():
    open("secret_book.txt","w").close()
    open("encrypted_messages.txt","w").close()

    