#!/usr/bin/python

import get_auth_token as auth
import json
import httplib

def list_servers(auth):
    adminURL="172.16.134.211:8774"
    headers= {"Content-type": "application/json","X-Auth-Token":auth.apitoken}
    url=auth.adminURL+'/servers/detail'
    #url="/v2/c382c329082f41528f26f310f88562ed/servers/detail"

    conn=httplib.HTTPConnection(adminURL)
    conn.request("GET",url,"",headers)
    response=conn.getresponse()
    code=response.status
    payload=response.read()
    payload_json=json.loads(payload)
    return payload_json
    

if __name__ == '__main__':
    url = "172.16.134.211:5000"
    osuser = "user_one"
    ospassword = "user_one"

    c=auth.OSAuth(url,osuser,ospassword)
    payload=list_servers(c)
    print json.dumps(payload,indent=4)
