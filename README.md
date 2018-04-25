# ifaceinfo
python script that return networks informations in json format

## compatibility
This script is compatible with Linux OS


## how this script work
The script read the '/sys/class/net/' recursively (partialy) and store the collected information in Dict and return the result that can be exploited like json file. 

## how to use it
```
python ifaceinfo.py
```

## how to use the class
```
under work
```

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
