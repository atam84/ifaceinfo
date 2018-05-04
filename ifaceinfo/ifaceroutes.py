import os
import sys
import time
from ifaceinfotools import IfaceInfoTools

class InterfacesRoutes(IfaceInfoTools):
    def __init__(self):
        """
        data initialisation
        maybe in the future somme other data will be loaded directly to improve performance and data usability
        at this time the scan of /sys/class/net are performed in the initialisation of the class
        """
        IfaceInfoTools
        self.version = '0.1.2'
        self.github_url = 'https://github.com/atam84/ifaceinfo'
        self.__timestamp = self.timestamp = int(time.time())
        self.__ifaces_routes = self.__get_routes('/proc/net/route')

    def __get_routes(self, routefile):
        # Iface	Destination	Gateway 	Flags	RefCnt	Use	Metric	Mask		MTU	Window	IRTT
        _routing = []
        try:
            """
            python 2 & 3 compatibility
            UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
            """
            if sys.version_info.major == 3:
                fd = open(routefile, 'r', encoding='latin1')
            else:
                fd = open(routefile, 'r')
            paramValue = fd.readlines()
        except IOError:
            paramValue = ''
            fd.close()
        if len(paramValue) == 1:
            return {}
        paramValue.pop(0)
        for route in paramValue:
            _route = route.split()
            _routing.append({
                'iface': _route[0],
                'x_dest': _route[1],
                'dest': self.reverse_ip(self.hex2ip(_route[1])),
                'x_gateway': _route[2],
                'gateway': self.reverse_ip(self.hex2ip(_route[2])),
                'flags': _route[3],
                'refcnt': _route[4],
                'use': _route[5],
                'metric': _route[6],
                'x_mask': _route[7],
                'mask': self.reverse_ip(self.hex2ip(_route[7])),
                'mtu': _route[8],
                'window': _route[9],
                'irtt': _route[10],
                'timestamp': self.__timestamp
            })
        return _routing

    def ifaces_routes(self):
        """
        return the routing table as array.
        """
        return self.__ifaces_routes

    def iface_routes(self, ifacename):
        """
        return the routing table of specific interface.
        """
        _iface_routes = []
        for iface_route in self.ifaces_routes():
            if iface_route['iface'] == 'ifacename':
                _iface_routes.append(iface_route)
        return _iface_routes




