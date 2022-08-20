#import the- required module
from cryptography.fernet import Fernet


#generate the key
key = Fernet.generate_key()

with open('unlock.key', 'rb') as unlock:
     key = unlock.read()
print(key)


#use the generated key
f = Fernet(key)
#open the original file to encrypt
with open('road.geojson', 'rb') as original_file:
     original = original_file.read()
#encrypt the file
encrypted = f.encrypt(original)
#you can write the encrypted data  file into a enc_sample.txt
with open ('road.geojson', 'wb') as encrypted_file:
     encrypted_file.write(encrypted)
