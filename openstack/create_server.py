#!/usr/bin/python

import get_auth_token as auth
import json
import httplib


url = "192.168.100.129:5000"
osuser = "user_one"
ospassword = "user_one"

c=auth.OSAuth(url,osuser,ospassword)
print c.apitoken
print c.tenant_id
print c.adminURL

adminURL="100.10.10.128:8774"
url="/v2/16f11babecae43a2863aee93135f3108/servers"
#params_init = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword}}}
params_init = {
  "server" : {
  "name" : "new-server-test",
  "imageRef" : "ab42bbcf-0aae-4999-815c-81be2cdf15f5",
  "flavorRef" : "1",
  "metadata" : {
    "My Server Name" : "Apache1"
  },
  "personality" : [
    {
      "path" : "/etc/banner.txt",
      "contents" : "ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBp \
dCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5k\
IGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVs\
c2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4g\
QnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRo\
ZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlv\
dSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vy\
c2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6\
b25zLiINCg0KLVJpY2hhcmQgQmFjaA=="
    }
  ]
  }
}


params = json.dumps(params_init)

headers= {"Content-type": "application/json","X-Auth-Token":c.apitoken}

conn=httplib.HTTPConnection(adminURL)
conn.request("POST",url,params,headers)
response=conn.getresponse()
code=response.status
payload=response.read()
payload_json=json.loads(payload)

print "return code is %s\n" % code
print json.dumps(payload_json,indent=4)


