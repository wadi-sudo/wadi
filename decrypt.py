#!C:\Users\Noureddine\AppData\Local\Programs\Python\Python37-32\python.exe


#import the- required module
from cryptography.fernet import Fernet



#generate the key
key = Fernet.generate_key()

with open('unlock.key', 'rb') as unlock:
     key = unlock.read()
#print(key)

#first use the key
f = Fernet(key)
#open the encrypted file
with open('road.geojson', 'rb') as encrypted_file:
     encrypted = encrypted_file.read()
#decrypt the file
decrypted = f.decrypt(encrypted)
#finally you can write the decrypted file into a dec_sample.txt
with open('road.geojson', 'wb') as decrypted_file:
     decrypted_file.write(decrypted)
