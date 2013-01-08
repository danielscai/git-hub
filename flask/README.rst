1. vm create api
===============

2. vm read api 
===============

2.1. Interface
-----------------
* GET::
    /zeus/iaas/api/system/vm/{availability_zone}/{management_zone}/{tenant_zone}/{vm_id}


2.2. Description:
-----------------

2.3. Interface parameter:
-----------------
none

2.4. Return value
-----------------

* HTTP response code:

2.5. Preparing Ubuntu 12.10
-----------------

* After you install Ubuntu 12.10 Server 64bits, Go to the sudo mode and don't leave it until the end of this guide::

   sudo su

3. Network Node
=========================

3.1. Preparing the Node
------------------

* Update your system::

   apt-get update
   apt-get upgrade
   apt-get dist-upgrade

* Install ntp service::

   apt-get install ntp

* Configure the NTP server to follow the controller node::
   
   sed -i 's/server ntp.ubuntu.com/server 100.10.10.51/g' /etc/ntp.conf
   service ntp restart  

* Install other services::

   apt-get install vlan bridge-utils

* Enable IP_Forwarding::

   nano /etc/sysctl.conf
   # Uncomment net.ipv4.ip_forward=1, to save you from rebooting, perform the following
   sysctl net.ipv4.ip_forward=1
