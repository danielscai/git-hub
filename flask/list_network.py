#!/usr/bin/python

import get_auth_token as auth
import json
import httplib
import re


url = "172.16.134.211:5000"
osuser = "dcai"
ospassword = "welcome1"

c=auth.OSAuth(url,osuser,ospassword)
print json.dumps(c.access,indent=4)

network_admin_url=c.access['serviceCatalog'][1]['endpoints'][0]['adminURL']

adminURL=network_admin_url
m=re.match(r'.*?/\/(.*?)\/',adminURL)
adminURL=m.group(1)

url=c.adminURL+"/networks"
print url
#params_init = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword}}}
params_init = {} 

params = json.dumps(params_init)

headers= {"Content-type": "application/json","X-Auth-Token":c.apitoken}
print headers

conn=httplib.HTTPConnection(adminURL)
conn.request("GET",url,'',headers)
response=conn.getresponse()
code=response.status
payload=response.read()
print payload
#payload_json=json.loads(payload)

print "return code is %s\n" % code
#print json.dumps(payload_json,indent=4)

