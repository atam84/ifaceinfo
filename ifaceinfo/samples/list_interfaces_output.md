### list_interface.py sample output

```
** interface name: br-74037696e854    id: 0x0     type: 1
      dev type       : bridge         operstate      : down        
      address        : 02:42:50:91:83:18      iface alias    :                       
      iface link     : 8                      iface index    : 8                     
      ip             : 10.0.32.1              mask           : 255.255.255.0         
      network        : 10.0.32.0              mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    0/0
        packets (tx/rx) :    0/0
        errors (tx/rx)  :    0/0


** interface name: docker0    id: 0x0     type: 1
      dev type       : bridge         operstate      : up          
      address        : 02:42:c8:45:72:15      iface alias    :                       
      iface link     : 5                      iface index    : 5                     
      ip             : 172.17.0.1             mask           : 255.255.0.0           
      network        : 172.17.0.0             mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    5095/3360
        packets (tx/rx) :    42/17
        errors (tx/rx)  :    0/0
    bridge connected interfaces:
        veth5c8bc65          22:dc:7d:c1:83:e1    up
        veth9de231e          a2:ff:7d:a6:d8:f1    up
        vethcd9b39d          66:68:b8:d6:13:32    up
        vethe69ab97          32:fa:f8:cb:7d:82    up


** interface name: vnet20    id: 0x0     type: 1
      dev type       : bridge         operstate      : down        
      address        : 02:42:6f:f7:74:5d      iface alias    :                       
      iface link     : 6                      iface index    : 6                     
      ip             : 192.168.20.254         mask           : 255.255.255.0         
      network        : 192.168.20.0           mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    0/0
        packets (tx/rx) :    0/0
        errors (tx/rx)  :    0/0


** interface name: usb0    id: 0x0     type: 1
      dev type       : unknown   operstate      : unknown     
      address        : 6a:a5:b1:1c:2d:30      iface alias    :                       
      iface link     : 15                     iface index    : 15                    
      ip             : 192.168.42.62          mask           : 255.255.255.0         
      network        : 192.168.42.0           mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    121385/746730
        packets (tx/rx) :    825/946
        errors (tx/rx)  :    0/0


** interface name: wlp2s0    id: 0x0     type: 1
      dev type       : wlan      operstate      : down        
      address        : 8c:a9:82:9d:7b:04      iface alias    :                       
      iface link     : 3                      iface index    : 3                     
      ip             :                        mask           :                       
      network        :                        mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    0/0
        packets (tx/rx) :    0/0
        errors (tx/rx)  :    0/0


** interface name: lo    id: 0x0     type: 772
      dev type       : unknown   operstate      : unknown     
      address        : 00:00:00:00:00:00      iface alias    :                       
      iface link     : 1                      iface index    : 1                     
      ip             : 127.0.0.1              mask           : 255.0.0.0             
      network        : 127.0.0.0              mtu            : 65536                 
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    825281/825281
        packets (tx/rx) :    11573/11573
        errors (tx/rx)  :    0/0


** interface name: br-5d11025eb09f    id: 0x0     type: 1
      dev type       : bridge         operstate      : down        
      address        : 02:42:0f:22:06:03      iface alias    :                       
      iface link     : 7                      iface index    : 7                     
      ip             : 192.168.16.254         mask           : 255.255.255.0         
      network        : 192.168.16.0           mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    0/0
        packets (tx/rx) :    0/0
        errors (tx/rx)  :    0/0


** interface name: veth8ad3bb3    id: 0x0     type: 1
      dev type       : unknown   operstate      : up          
      address        : da:af:5d:0d:ce:10      iface alias    :                       
      iface link     : 13                     iface index    : 14                    
      ip             : 169.254.139.224        mask           : 255.255.0.0           
      network        : 169.254.0.0            mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    116291/790
        packets (tx/rx) :    430/3
        errors (tx/rx)  :    0/0
    device connected on bridge:
        docker_gwbridge      02:42:47:11:e5:01    up


** interface name: veth5c8bc65    id: 0x0     type: 1
      dev type       : unknown   operstate      : up          
      address        : 22:dc:7d:c1:83:e1      iface alias    :                       
      iface link     : 16                     iface index    : 17                    
      ip             : 169.254.176.24         mask           : 255.255.0.0           
      network        : 169.254.0.0            mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    18512/966
        packets (tx/rx) :    119/5
        errors (tx/rx)  :    0/0
    device connected on bridge:
        docker0              02:42:c8:45:72:15    up


** interface name: enp5s0    id: 0x0     type: 1
      dev type       : unknown   operstate      : down        
      address        : f0:bf:97:61:fa:a9      iface alias    :                       
      iface link     : 2                      iface index    : 2                     
      ip             :                        mask           :                       
      network        :                        mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    0/0
        packets (tx/rx) :    0/0
        errors (tx/rx)  :    0/0


** interface name: docker_gwbridge    id: 0x0     type: 1
      dev type       : bridge         operstate      : up          
      address        : 02:42:47:11:e5:01      iface alias    :                       
      iface link     : 4                      iface index    : 4                     
      ip             : 172.18.0.1             mask           : 255.255.0.0           
      network        : 172.18.0.0             mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    11792/748
        packets (tx/rx) :    127/3
        errors (tx/rx)  :    0/0
    bridge connected interfaces:
        veth8ad3bb3          da:af:5d:0d:ce:10    up


** interface name: vethcd9b39d    id: 0x0     type: 1
      dev type       : unknown   operstate      : up          
      address        : 66:68:b8:d6:13:32      iface alias    :                       
      iface link     : 18                     iface index    : 19                    
      ip             :                        mask           :                       
      network        :                        mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    9047/876
        packets (tx/rx) :    46/4
        errors (tx/rx)  :    0/0
    device connected on bridge:
        docker0              02:42:c8:45:72:15    up


** interface name: veth9de231e    id: 0x0     type: 1
      dev type       : unknown   operstate      : up          
      address        : a2:ff:7d:a6:d8:f1      iface alias    :                       
      iface link     : 20                     iface index    : 21                    
      ip             :                        mask           :                       
      network        :                        mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    8257/966
        packets (tx/rx) :    43/5
        errors (tx/rx)  :    0/0
    device connected on bridge:
        docker0              02:42:c8:45:72:15    up


** interface name: vethe69ab97    id: 0x0     type: 1
      dev type       : unknown   operstate      : up          
      address        : 32:fa:f8:cb:7d:82      iface alias    :                       
      iface link     : 22                     iface index    : 23                    
      ip             :                        mask           :                       
      network        :                        mtu            : 1500                  
    interface statistics:
        multicast       :    0          collisions      :  0
        bytes (tx/rx)   :    6770/790
        packets (tx/rx) :    38/3
        errors (tx/rx)  :    0/0
    device connected on bridge:
        docker0              02:42:c8:45:72:15    up


---------------

14 network interfaces that include 5 bridge listed
7 up, 5 down and 2 with unknown status.

---------------
```