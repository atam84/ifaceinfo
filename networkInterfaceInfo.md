### class networkInterfaceInfo
   	  	Methods defined here:

#### __init__(self)
    data initialisation
    maybe in the future somme other data will be loaded directly to improve performance and data usability

#### getIfaceInfo(self, path)
    the main function that scan /sys/class/net to collect interfaces informations

#### get_ipAddress(self, ifaceName)
    get ip address of interface using socket interface

#### get_networkAddress(self, ipaddr, mask)

#### get_networkMask(self, ifaceName)
    get net mask address of interface using socket interface

#### getifaceByIndex(self, ifindex, info='full')
    get interface that have ifindex=X
    ifindex is located in /sys/class/net/<iface>/ifindex
    return an array with dict

#### getifaceByInterfaceUID(self, identifier, value, info='full')
    get interfaces by defined identifier and value, the third parametre info allow 
    the choise to return the result as a full data or briefly
     
    the identifier can be any key value of the class definition
    this funtion is used by self.getifaceByIndex() and self.getifaceByLink()
     
    return an array of dict

#### getifaceByLink(self, iflink, info='full')
    get interface that have iflink=X
    ifindex is located in /sys/class/net/<iface>/iflink
    return an array with dict

#### getifaceInfo(self, ifaceName)
    get specific interface name with full information
    return dict

#### getifacesByStatus(self, status, info='full')
    get interface by status, this function is used by self.getifacesUp() and self.getifacesDown()
    return an array with dict

#### getifacesDown(self, info='full')
    get interface down and other status
    return an array with dict

#### getifacesIndex(self)
    get all interfaces name and ifindex
    return array of dict

#### getifacesIndexLink(self)
    get all interfaces with brief informations (name, ifindex, iflink, ip and mask)
    return an array of dict

#### getifacesInfo(self)
    get all interfaces informations (full collected information)

#### getifacesLink(self)
    get all interfaces name and iflink
    return array of dict

#### getifacesUp(self, info='full')
    get interface up only
    return an array with dict

#### hex2ip(self, x_addr)
    convert hexadecimal representation to string decimal ip address
    return string (as ip address representation)

#### ifacesCount(self)
    return a number of detected interfaces

#### ifacesList(self)
    get a list of interface name
    return array of string

#### ip2hex(self, addr)
    convert string decimal ip address to hexadecimal representation
    return string (as hex representation)

#### refresh(self)
    this function refresh the informations collected when the class is loaded
    if you want to work with fresh data use the function to reload the data updated

#### reload(self)
    same as self.refresh()

#### scan_object(self, path, object_name)
    function used to scan the first level of sub directories in /sys/class/net/<iface>/
