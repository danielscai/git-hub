#!/usr/bin/python 
import json
from flask import Flask,request

from os_mid_api import OSMA


app = Flask(__name__)
url = "172.16.134.212:5000"
osuser = "admin"
ospassword = "admin_pass"

os=OSMA(url,osuser,ospassword)


### sytem vm api 

@app.route("/zeus/iaas/api/system/vm/<availability_zone>/<management_zone>/<tenant_zone>/<vm_id>", 
    methods=[ 'GET','POST','PUT','DELETE'])
def vm_fun(availability_zone,management_zone,tenant_zone,vm_id):
    ''' system vm associated functions'''
    if request.method == 'GET':
        ret_json=os.read_server(vm_id)
        return ret_json

    elif request.method == 'POST':
        vm_name=vm_id
        payload=request.data
        ret_json=os.create_server(vm_name,payload)
        return ret_json

    elif request.method == 'PUT':
        payload=request.data
        ret_json=os.update_server(vm_id,payload)
        return ret_json

    elif request.method == 'DELETE':
        ret_json=os.delete_server(vm_id)
        print 'delete'
        return ret_json

    else:
        params={'availability_zone':availability_zone,
            'management_zone':management_zone,
            'tenant_zone':tenant_zone,
            'vm_id':vm_id,
            'request method':request.method,
        }
        ret_json=json.dumps(params)
        return ret_json

### test if api works
@app.route('/list')
def list_servers():
    servers=os.list_servers()
    return servers

@app.route("/")
def hello():
    return "It works!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088,debug=True)
