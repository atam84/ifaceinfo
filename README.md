# ifaceinfo
python package that provide networks informations in json/dict format

##### Informations are collected:
- network device name
- mac addr, ip addr, mask, network addr
- status
- statistics
- ifindex, iflink
- routing table
- tcp and tcpv6 connexions
- udp and udpv6 connexions
- ...
#### Take a look to the samples informations collected
- [interfaces](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/outputs_examples/test_ifacesinfos.md)
- [routing table](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/outputs_examples/test_routes.md)
- [tcp connexion](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/outputs_examples/test_tcp.md)
- [udp connexion](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/outputs_examples/test_udp.md)


## Version: 0.1.7, python compatibility: Python 2 and Python 3

## compatibility
This script is compatible with Linux OS


## how this script work
The script read the '/sys/class/net/' recursively (partialy) and store the collected information in Dict and return the result that can be exploited like json file. 

## how to install
```
pip install ifaceinfo
```
or clone the github repository and work directly with

## how to use the class
```python
from ifaceinfo import InterfacesInfos
from ifaceroutes import InterfacesRoutes
from ifaceroutes import TCPConn
from ifaceroutes import UDPConn

ifaces = InterfacesInfos()
ifacesroutes = InterfacesRoutes()
tcpconn = TCPConn()
udpconn = UDPConn()
```

### class documentations
- [InterfacesInfos](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/doc/ifaceinfo.md#class-interfacesinfos)
- [InterfacesRoutes](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/doc/ifaceroutes.md#class-interfacesroutes)
- [TCPConn](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/doc/udpconn.md#class-tcpconn)
- [UDPConn](https://github.com/atam84/ifaceinfo/blob/master/ifaceinfo/doc/udpconn.md#class-udpconn)



## for more informations about the keyword signification read this:
https://www.kernel.org/doc/Documentation/ABI/testing/
- [sysfs-class-net](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net)
- [sysfs-class-net-batman-adv](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-batman-adv)
- [sysfs-class-net-cdc_ncm](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-cdc_ncm)
- [sysfs-class-net-grcan](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-grcan)
- [sysfs-class-net-janz-ican3](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-janz-ican3)
- [sysfs-class-net-mesh](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-mesh)
- [sysfs-class-net-phydev](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-phydev)
- [sysfs-class-net-qmi](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-qmi)
- [sysfs-class-net-queues](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-queues)
- [sysfs-class-net-statistics](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net-statistics)
