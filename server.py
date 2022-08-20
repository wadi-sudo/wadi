from cryptography.fernet import Fernet
import os
import datetime
from flask import Flask, redirect, url_for, render_template

import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from filelock import FileLock


def limit_time():
    current = time.time()

    one_year = 1314000
 
    limit = 1661015640  

    if os.path.exists('static/test.txt'):
        print('yes')
        if current >= limit :
            os.remove("static/test.txt")


scheduler = BackgroundScheduler()
scheduler.add_job(func=limit_time, trigger="interval", seconds=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

















lockfile = open("static/road.geojson", "r")
lockfile.flush()
lock = FileLock(r"static/road.geojson" + ".lock")

with lock:



    app = Flask(__name__)



    @app.before_first_request
    def before_request_func():
        #key = Fernet.generate_key()
        with open('static/unlock.key', 'rb') as unlock:
            key = unlock.read()

        f = Fernet(key)
    #open the encrypted file
        with open('static/road.geojson', 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
    #decrypt the file
        decrypted = f.decrypt(encrypted)
    #finally you can write the decrypted file into a dec_sample.txt
        with open('static/test.geojson', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        print('welcome')
    











    @app.route("/")
    def home():
        return render_template("index.html")




    if __name__ == "__main__":
        app.run()



    '''with open('static/unlock.key', 'rb') as unlock:
         key = unlock.read()
#print(key)


#use the generated key
    f = Fernet(key)
#open the original file to encrypt
    with open('static/road.geojson', 'rb') as original_file:
         original = original_file.read()
#encrypt the file
    encrypted = f.encrypt(original)
#you can write the encrypted data  file into a enc_sample.txt
    with open ('static/road.geojson', 'wb') as encrypted_file:
         encrypted_file.write(encrypted)'''

os.remove("static/test.geojson")





'''@app.after_request
def after_request_func(response):
    with open('static/unlock.key', 'rb') as unlock:
        key = unlock.read()

    f = Fernet(key)

    with open('static/road.geojson', 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open ('static/road.geojson', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)  
    print ('done')
    return(response)'''



'''def encrypt():
    with open('static/unlock.key', 'rb') as unlock:
        key = unlock.read()

    f = Fernet(key)

    with open('static/road.geojson', 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open ('static/road.geojson', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)  
    print ('done')


'''