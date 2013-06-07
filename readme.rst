
==================================================
zeusapi 后台脚本部署文档
==================================================

:作者: 蔡云飞 daniels.cai@lecast.com.cn


.. footer:: zeus 开发团队文档 - 2013-06-07


1. 部署rbd限速脚本
-----------------------
1.1. 添加模块
#####################
* 在 ``/etc/modules`` 文件末尾添加 ::

    cls_cgroup

1.2. 挂载cgroup文件系统
########################

* 在 /etc/rc.local文件中添加如下代码 ::

    mkdir -p /sys/fs/cgroup/net_cls
    mount -t cgroup -o net_cls none /sys/fs/cgroup/net_cls

1.3. 签出最新代码
######################## 
* 签出最新代码 ::

    cd /opt
    git clone git@telive.unfuddle.com:telive/zeusscripts.git

1.4. 部署到upstart job
########################

* copy到/etc/init ::

    cp /opt/zeusscripts/libvirt-monitor/libvirt-monitor.conf /etc/init
    cp /opt/zeusscripts/libvirt-monitor/limit-rrd-rate/limit-rrd-rate.conf /etc/init

    start libvirt-monitor
    start limit-rrd-rate


1.5. 检查状态
########################

* 使用status 查看状态 ::

    status libvirt-monitor
    status limit-rrd-rate
