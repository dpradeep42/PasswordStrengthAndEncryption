import re

from cryptography.fernet import Fernet


def encryption(text):
    try:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        print(text)
        enctext = fernet.encrypt(text.encode())
        print(enctext)
        dectext = fernet.decrypt(enctext).decode()
        print(dectext)
    except:
        print("Error occured in Excryption")

def textvalidation(text):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&=+-_])[A-Za-z\d@$!#%*?&=+-_]{8,}$'
    if re.search(re.compile(regex), text):
        encryption(text)
    else:
        print("Text Doesnt met the requirement")


if __name__ == '__main__':
    textvalidation(input("Enter a text: "))
