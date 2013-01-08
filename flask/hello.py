#!/usr/bin/python 


import json
from flask import Flask,request

from os_mid_api import OSMA


app = Flask(__name__)
url = "172.16.134.211:5000"
osuser = "user_one"
ospassword = "user_one"

os=OSMA(url,osuser,ospassword)

@app.route("/")
def hello():
    return "It works!"

### sytem api 

@app.route("/zeus/iaas/api/system/vm/<availability_zone>/<management_zone>/<tenant_zone>/<vm_id>", 
    methods=[ 'GET','POST','PUT','DELETE'])
def vm_fun(availability_zone,management_zone,tenant_zone,vm_id):
    params={'availability_zone':availability_zone,
        'management_zone':management_zone,
        'tenant_zone':tenant_zone,
        'vm_id':vm_id,
        'request method':request.method,
    }
    ret_json=json.dumps(params)

    if request.method == 'GET':
        ret=os.read_server(vm_id)
        return ret

    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return ret_json
    return ret_json

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088,debug=True)
