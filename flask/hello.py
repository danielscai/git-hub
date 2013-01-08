#!/usr/bin/python 

from flask import Flask
import json

import os_api as os

app = Flask(__name__)
url = "172.16.134.211:5000"
osuser = "user_one"
ospassword = "user_one"

auth=os.login(url,osuser,ospassword)

@app.route("/")
def hello():
    return "It works!"
def world():
    return 'is is world!'

@app.route("/list")
def list_servers():
    payload=os.list_servers(auth)
    return payload

@app.route("/create")
def create_server():
    payload=os.create_server(auth)
    return payload

@app.route("/zeus/iaas/api/system/vm/{availability_zone}/{management_zone}/{tenant_zone}/{vm_id}", methods=['GET', 'POST','PUT','DELETE'])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088,debug=True)
