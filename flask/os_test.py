#!/usr/bin/python 

from os_mid_api import OSMA

url = "172.16.134.211:5000"
osuser = "user_one"
ospassword = "user_one"

vm_id='817ff98f-0b8c-4cc7-a290-04b252cf7249'

os=OSMA(url,osuser,ospassword)
server=os.read_server(vm_id)
print server



