#!/usr/bin/python

import get_auth_token as auth
import json
import httplib


url = "172.16.134.211:5000"
osuser = "user_one"
ospassword = "user_one"

c=auth.OSAuth(url,osuser,ospassword)
print c.apitoken
print c.tenant_id
print c.adminURL

adminURL="172.16.134.211:8774"
url="/v2/c382c329082f41528f26f310f88562ed/servers/detail"
#self.params_init = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword}}}
#self.params = json.dumps(self.params_init)
headers= {"Content-type": "application/json","X-Auth-Token":c.apitoken}

conn=httplib.HTTPConnection(adminURL)
conn.request("GET",url,"",headers)
response=conn.getresponse()
code=response.status
payload=response.read()
payload_json=json.loads(payload)

print "return code is %s\n" % code
print json.dumps(payload_json,indent=4)

