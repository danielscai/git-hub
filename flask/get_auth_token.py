#!/usr/bin/python

import httplib
import json


class OSAuth:
  import httplib
  import json
  ''' Get Authed from openstack API '''
  def __init__(self,url,osuser,ospassword):
    self.url=url
    self.osuser=osuser
    self.ospassword=ospassword

    self.params_init = {"auth":{"passwordCredentials":{"username":osuser, "password":ospassword}}}
    self.params = json.dumps(self.params_init)
    self.headers= {"Content-type": "application/json"}

    self.conn = httplib.HTTPConnection(url)
    self.get_token_init()
    self.get_tenant_id()
    self.get_token()

  def get_token_init(self):
    conn=self.conn
    conn.request("POST", "/v2.0/tokens", self.params, self.headers)
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)
    self.apitoken = dd['access']['token']['id']

  def get_tenant_id(self):
    conn=self.conn
    self.params_init['auth']['tenantId']=''
    self.params = json.dumps(self.params_init)
    self.headers['X-Auth-Token']=self.apitoken
    conn.request("GET","/v2.0/tenants",self.params,self.headers)
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)
    self.tenant_id=dd['tenants'][0]['id']
    return self.tenant_id

  def get_token(self):
    conn=self.conn
    self.params_init['auth']['tenantId']=self.tenant_id
    self.params = json.dumps(self.params_init)
    del self.headers['X-Auth-Token']
    conn.request("POST", "/v2.0/tokens", self.params, self.headers)
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)
    self.resp=dd
    self.apitoken=self.resp['access']['token']['id']
    self.adminURL=self.resp['access']['serviceCatalog'][0]['endpoints'][0]['adminURL']
    return self.apitoken

  def http_post(self,url):
    conn=self.conn
    params=self.params
    headers=self.headers
    conn.request("POST",url,params,headers)
    response=conn.getresponse()
    payload=response.read()
    payload_json=json.loads(payload)
    return payload_json


  def __destroy__(self):
    self.conn.close()
   
if __name__ == '__main__':
  #url = "192.168.100.129:5000"
  url = "172.16.134.211:5000"
  osuser = "user_one"
  ospassword = "user_one"

  c=OSAuth(url,osuser,ospassword)
  print c.apitoken
  print c.tenant_id
