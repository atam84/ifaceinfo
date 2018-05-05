# Package ifaceroutes Documentation

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




## Class InterfacesRoutes
None
### \_\_init\_\_
```py

def __init__(self)

```



data initialisation
maybe in the future somme other data will be loaded directly to improve performance and data usability
at this time the scan of /sys/class/net are performed in the initialisation of the class


### hex2ip
```py

def hex2ip(self, x_addr)

```



private methode
convert hexadecimal representation to string decimal ip address
return string (as ip address representation)


### iface\_routes
```py

def iface_routes(self, ifacename)

```



return the routing table of specific interface.


### ifaces\_routes
```py

def ifaces_routes(self)

```



return the routing table as array.


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




