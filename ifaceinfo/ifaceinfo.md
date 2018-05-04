# NAME
#### ifaceinfo

# FILE
#### ifaceinfo.py

# CLASSES
## InterfacesInfos

# class InterfacesInfos

## Methods defined here:


### __init__(self)
```
data initialisation

maybe in the future somme other data will be loaded directly to improve performance and data usability

at this time the scan of /sys/class/net are performed in the initialisation of the class
```

### as_dict(self)
```
return interfaces informations as dict result
```

### get_timestamp(self)
```
get timestamp of data collection
```

### iface_as_dict(self, ifacename)
```
return interfaces informations as dict result
```

### iface_by_ifindex(self, ifindex, info='full')
```
get interface that have ifindex=X

ifindex is located in /sys/class/net/<iface>/ifindex

return dict
```

### iface_by_iflink(self, iflink, info='full')
```
get interface that have iflink=X

ifindex is located in /sys/class/net/<iface>/iflink

return dict
```

### iface_by_uid(self, identifier, value, info='full')
```
get interfaces by defined identifier and value, the third parametre info allow 

the choise to return the result as a full data or briefly

the identifier can be any key value of the class definition

this funtion is used by self.getifaceByIndex() and self.getifaceByLink()

return dict
```

### iface_info(self, ifaceName)
```
get specific interface name with full information

return dict
```

### iface_network_config(self, ifacename)
```
get specific interface network configuration only, return dict
```

### iface_routes(self, ifacename)
```
return the routing table of specific interface.
```

### iface_statistics(self, ifacename)
```
return a dict of specific interface with statistics
```

### iface_type(self, ifacename)
```
return a dict of specific interface with interface_type if the interface is not found return empty dict
```

### ifaces_as_dict(self)
```
return interfaces informations as dict result give the same result as self.as_dict()
```

### ifaces_by_status(self, status, info='full')
```
get interface by status, this function is used by self.getifacesUp() and self.getifacesDown()

return an array with dict
```

### ifaces_count(self)
```
return a number of detected interfaces
```

### ifaces_down(self, info='full')
```
get interface down and other status

return an array with dict
```

### ifaces_ifindex(self)
```
get all interfaces name and ifindex

return array of dict
```

### ifaces_ifindex_iflink(self)
```
get all interfaces with brief informations (name, ifindex, iflink, ip and mask)

return an array of dict
```

### ifaces_iflink(self)
```
get all interfaces name and iflink

return array of dict
```

### ifaces_info(self)
```
get all interfaces informations (full collected information)
```

### ifaces_list(self)
```
get a list of interface name

return array of string
```

### ifaces_network_config(self)
```
get the interfaces network configuration only
```

### ifaces_routes(self)
```
return the routing table as array.
```

### ifaces_statistics(self)
```
return a list of all interfaces with statistics
```

### ifaces_statistics_as_dict(self)
```
return ifaces statistics as dict
```

### ifaces_type(self)
```
return a list of all interfaces with uevent that give device type
```

### ifaces_up(self, info='full')
```
get interface up only

return an array with dict
```

### list_interfaces(self)
```
list interfaces name from dict, this is like self.ifaces_list()
```

### refresh(self)
```
this function refresh the informations collected when the class is loaded

if you want to work with fresh data use the function to reload the data updated
```

### reload(self)
```
same as self.refresh()
```
