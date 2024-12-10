from getpass import getpass
from getfile  import getfile
from playfile import playfile

file = 'sousa.au'                     
site = 'ftp.rmi.net'                  
dir  = '.'
user = ('lutz', getpass('Pswd?'))

getfile(file, site, dir, user)        
playfile(file)                        

# import os
# os.system('getone.py sousa.au')     