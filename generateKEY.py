#import the- required module
from cryptography.fernet import Fernet


#generate the key
key = Fernet.generate_key()
#string the key into a file
with open('unlock.key', 'wb') as unlock:
    unlock.write(key)

#open the key
with open('unlock.key', 'rb') as unlock:
     key = unlock.read()
print(key)
