#!/usr/bin/python

import base64
import urllib
import httplib
import json
import os
from urlparse import urlparse

### --8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--
###
###  insert the 'Get OpenStack Credentials' snippet here
url = "192.168.100.129:5000"
osuser = "user_one"
ospassword = "user_one"
params = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword},'tenantId':"16f11babecae43a2863aee93135f3108"}}
params = json.dumps(params)
headers= {"Content-type": "application/json"}
conn = httplib.HTTPConnection(url)
conn.request("POST", "/v2.0/tokens", params, headers)
# HTTP response

response = conn.getresponse()
data = response.read()
dd = json.loads(data)
conn.close()

print json.dumps(dd,indent=4)
exit ()
apitoken = dd['access']['token']['id']

#apiurl = dd['access']['serviceCatalog']['nova'][0]['publicURL']
#apiurlt = urlparse(dd['access']['serviceCatalog']['nova'][0]['publicURL'])

###
### --8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--8<--

###
### Get the list of server IP addresses
###

# HTTP connection #2

srvID = 1       # server ID number
url2 = apiurlt[1]
params2 = urllib.urlencode({})
headers2 = { "X-Auth-Token":apitoken, "Content-type":"application/json" }

if (usehttps == True):
    conn2 = httplib.HTTPSConnection(url2, key_file='../cert/priv.pem', cert_file='../cert/srv_test.crt')
else:
    conn2 = httplib.HTTPConnection(url2)

conn2.request("GET", "%s/servers/%s/ips" % (apiurlt[2], srvID), params2, headers2)

# HTTP response #2

response2 = conn2.getresponse()
data2 = response2.read()
dd2 = json.loads(data2)

conn2.close()

print dd2
