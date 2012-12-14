#!/usr/bin/python

import httplib
import json

# arguments


url = "192.168.100.129:5000"
osuser = "user_one"
ospassword = "user_one"
params = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword}}}
params = json.dumps(params)
headers= {"Content-type": "application/json"}
conn = httplib.HTTPConnection(url)
conn.request("POST", "/v2.0/tokens", params, headers)
# HTTP response

response = conn.getresponse()
data = response.read()
dd = json.loads(data)

conn.close()

apitoken = dd['access']['token']['id']

print "Your token is: %s" % apitoken
