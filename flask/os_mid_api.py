#!/usr/bin/python

import httplib
import json 
import re

class OSMA:
  def __init__(self,url,osuser,ospassword):
    self.auth=OSAuth(url,osuser,ospassword) 
    self.conn=httplib.HTTPConnection(self.auth.adminURI)
    
  def read_server(self,vm_id):
    '''read a specific vm's infomation, 
    id of the vm should be provided'''

    fun_url='/servers' +'/' + vm_id
    payload=self.request('GET',fun_url)
    payload=self.format_to_zeus(payload)
    return payload

  def list_servers(self):
    ''' list all servers, for debug use, 
    not included in develop docs'''

    fun_url='/servers'
    payload=self.request('GET',fun_url)
    return payload

  def create_server(self,vm_name,params):
    ''' create server in openstack'''
    
    fun_url='/servers'
    params_init = {
      "server" : {
        "name" : vm_name,
        "imageRef" : "7f5bc981-0aba-41c1-9d7e-f067e5b5aef4",
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
    payload=self.request('POST',fun_url,params)
    return payload


  def request(self,method,fun_url,params='',headers=''):
    ''' handle http request '''

    # to-do: headers should be user set when not blenk
    conn=self.conn
    url=self.auth.adminURL + fun_url
    headers= {"Content-type": "application/json",
        "X-Auth-Token":self.auth.apitoken}
    conn.request(method,url,params,headers)
    response=conn.getresponse()
    code=response.status
    payload=response.read()
    return payload

  def format_to_zeus(self,os_payload):
    ''' formate openstack payload to zeus payload,
    refer develop documentation for more details'''
  
    os_data=json.loads(os_payload)
    server=os_data['server']
    zeus_data_tmp={}

    zeus_data_tmp['vm_name']=server['name']
    zeus_data_tmp['status']=server['status']
    zeus_data_tmp['created_time']=server['created']
    zeus_data_tmp['updated_time']=server['updated']
    zeus_data_tmp['metadata']=server['metadata']
    zeus_data_tmp['security_groups']=server['security_groups']
    zeus_data_tmp['access_ip']=server['accessIPv4']
    zeus_data_tmp['network']=server['addresses']

    zeus_data_tmp['image']={}
    zeus_data_tmp['image']['id']=server['image']['id']

    zeus_data_tmp['config']={}
    zeus_data_tmp['config']['id']=server['image']['id']

    zeus_data_tmp['host']={}
    zeus_data_tmp['host']['id']=server['hostId']

    zeus_data_tmp['user']={}
    zeus_data_tmp['user']['id']=server['user_id']

    zeus_data={'vm':zeus_data_tmp}
    zeus_payload=json.dumps(zeus_data)
    return zeus_payload
    
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
    m=re.match(r'.*?/\/(.*?)\/',self.adminURL)
    self.adminURI=m.group(1)
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
