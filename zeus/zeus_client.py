#!/usr/bin/python 

import httplib
import json


if __name__ == "__main__":

    zeus_api_server='172.16.134.212:8088'
    create_server_url="/zeus/iaas/api/system/vm/data-center1/os-management1/tenant1/api_create_test"

    vm_info={
        "vm": {
            "config_id": "1",
            "vm_config": {
                "cpuCount":"1",
                "memorySize":"512",
                "diskSize":"20"
             },
            "host":    "3bdc1a0c5daf1c07eed35d887d35aca6af97aac42e0bbac507ebf57e",
            "image_id": "447ba47b-b40c-4aff-8d55-d6e19c1f8a85",
            "metadata": {
                "My Server Name": "Apache1"
            },
            "nic": [
                {"network":"d2ce5263-54d1-4208-acfa-e98810f4db5d",
                 "ip_addr":"192.168.1.1",
                 "port":"port_id"}
                ],
            "security_zone": [
            {
                "name": "default"
            }
            ],
            "ssh_options":{
                "public_key":"key_id",
                "private_key":"key_id",
                "authorized_keys":"key_id"
            }
        }
    }

    params=json.dumps(vm_info)
    print "send \n"
    print json.dumps(vm_info,indent=4)

    headers= {"Content-type": "application/json"}

    conn=httplib.HTTPConnection(zeus_api_server)
    conn.request("POST",create_server_url,params,headers)

    response=conn.getresponse()
    code=response.status
    payload=response.read()
    payload_json=json.loads(payload)

    print json.dumps(payload_json,indent=4)

