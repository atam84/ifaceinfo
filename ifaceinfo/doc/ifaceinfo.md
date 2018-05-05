# Package ifaceinfo Documentation

## Class IfaceInfoTools
None
### \_\_init\_\_
```py

def __init__(self)

```



### hex2ip
```py

def hex2ip(self, x_addr)

```



private methode
convert hexadecimal representation to string decimal ip address
return string (as ip address representation)


### ip2hex
```py

def ip2hex(self, addr)

```



private methode
convert string decimal ip address to hexadecimal representation
return string (as hex representation)


### ip\_address
```py

def ip_address(self, ifacename)

```



private methode
get ip address of interface using socket interface


### network\_address
```py

def network_address(self, ipaddr, mask)

```



private methode
used to calculate the network address


### network\_mask
```py

def network_mask(self, ifacename)

```



private methode
get net mask address of interface using socket interface


### reverse\_ip
```py

def reverse_ip(self, ipaddress)

```



Private method that reverse ip address




## Class InterfacesInfos
None
### \_\_init\_\_
```py

def __init__(self)

```



data initialisation
maybe in the future somme other data will be loaded directly to improve performance and data usability
at this time the scan of /sys/class/net are performed in the initialisation of the class


### as\_dict
```py

def as_dict(self)

```



return interfaces informations as dict result


### get\_timestamp
```py

def get_timestamp(self)

```



get timestamp of data collection


### hex2ip
```py

def hex2ip(self, x_addr)

```



private methode
convert hexadecimal representation to string decimal ip address
return string (as ip address representation)


### iface\_as\_dict
```py

def iface_as_dict(self, ifacename)

```



return interfaces informations as dict result


### iface\_by\_ifindex
```py

def iface_by_ifindex(self, ifindex, info='full')

```



get interface that have ifindex=X
ifindex is located in /sys/class/net/<iface>/ifindex
return dict


### iface\_by\_iflink
```py

def iface_by_iflink(self, iflink, info='full')

```



get interface that have iflink=X
ifindex is located in /sys/class/net/<iface>/iflink
return dict


### iface\_by\_uid
```py

def iface_by_uid(self, identifier, value, info='full')

```



get interfaces by defined identifier and value, the third parametre info allow 
the choise to return the result as a full data or briefly

the identifier can be any key value of the class definition
this funtion is used by self.getifaceByIndex() and self.getifaceByLink()

return dict


### iface\_info
```py

def iface_info(self, ifaceName)

```



get specific interface name with full information
return dict


### iface\_network\_config
```py

def iface_network_config(self, ifacename)

```



get specific interface network configuration only, return dict


### iface\_routes
```py

def iface_routes(self, ifacename)

```



return the routing table of specific interface.


### iface\_statistics
```py

def iface_statistics(self, ifacename)

```



return a dict of specific interface with statistics


### iface\_type
```py

def iface_type(self, ifacename)

```



return a dict of specific interface with interface_type if the interface is not found return empty dict


### ifaces\_as\_dict
```py

def ifaces_as_dict(self)

```



return interfaces informations as dict result give the same result as self.as_dict()


### ifaces\_by\_status
```py

def ifaces_by_status(self, status, info='full')

```



get interface by status, this function is used by self.getifacesUp() and self.getifacesDown()
return an array with dict


### ifaces\_count
```py

def ifaces_count(self)

```



return a number of detected interfaces


### ifaces\_down
```py

def ifaces_down(self, info='full')

```



get interface down and other status
return an array with dict


### ifaces\_ifindex
```py

def ifaces_ifindex(self)

```



get all interfaces name and ifindex
return array of dict


### ifaces\_ifindex\_iflink
```py

def ifaces_ifindex_iflink(self)

```



get all interfaces with brief informations (name, ifindex, iflink, ip and mask)
return an array of dict


### ifaces\_iflink
```py

def ifaces_iflink(self)

```



get all interfaces name and iflink
return array of dict


### ifaces\_info
```py

def ifaces_info(self)

```



get all interfaces informations (full collected information)


### ifaces\_list
```py

def ifaces_list(self)

```



get a list of interface name
return array of string


### ifaces\_network\_config
```py

def ifaces_network_config(self)

```



get the interfaces network configuration only


### ifaces\_routes
```py

def ifaces_routes(self)

```



return the routing table as array.


### ifaces\_statistics
```py

def ifaces_statistics(self)

```



return a list of all interfaces with statistics


### ifaces\_statistics\_as\_dict
```py

def ifaces_statistics_as_dict(self)

```



return ifaces statistics as dict


### ifaces\_type
```py

def ifaces_type(self)

```



return a list of all interfaces with uevent that give device type


### ifaces\_up
```py

def ifaces_up(self, info='full')

```



get interface up only
return an array with dict


### ip2hex
```py

def ip2hex(self, addr)

```



private methode
convert string decimal ip address to hexadecimal representation
return string (as hex representation)


### ip\_address
```py

def ip_address(self, ifacename)

```



private methode
get ip address of interface using socket interface


### list\_interfaces
```py

def list_interfaces(self)

```



list all interafces as list()


### network\_address
```py

def network_address(self, ipaddr, mask)

```



private methode
used to calculate the network address


### network\_mask
```py

def network_mask(self, ifacename)

```



private methode
get net mask address of interface using socket interface


### refresh
```py

def refresh(self)

```



this function refresh the informations collected when the class is loaded
if you want to work with fresh data use this function to reload the data updated


### reload
```py

def reload(self)

```



same as self.refresh()


### reverse\_ip
```py

def reverse_ip(self, ipaddress)

```



Private method that reverse ip address




