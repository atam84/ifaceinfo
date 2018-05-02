# ifaceinfo
python script that return networks informations in json format.
the informations collected:
- network name
- mac, ip, mask, network address
- status
- statistics
- ifindex, iflink
- routing table

#### comming soon:
- tcp/tcp6 established connexion
- udp/udp6 established connexion

## Version: 0.1.2, python compatibility: Python 2 and Python 3

## compatibility
This script is compatible with Linux OS


## how this script work
The script read the '/sys/class/net/' recursively (partialy) and store the collected information in Dict and return the result that can be exploited like json file. 

## how to use it
```
python ifaceinfo.py
```

## how to use the class
```python
from ifaceinfo import InterfacesInfos

ifaces = InterfacesInfos()
```
[View the full documentation](networkInterfaceInfo.md)


## output example
[Output example](output.md)


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
