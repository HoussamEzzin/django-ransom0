from django.shortcuts import render
from .models import Client
import os
import ssl
import time
import requests
import subprocess
from datetime import datetime
from os import name, path 
from cryptography.fernet import Fernet
from random import randint

#global variables

digits = randint(1111,9999)
key = Fernet.generate_key()




def home(request):
    return render(request,'ransom0/home.html')
