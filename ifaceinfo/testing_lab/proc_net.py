#!/usr/bin/env python

import socket
import fcntl
import struct
from pprint import pprint
'''
   0            1            2                                            7
   v            v            v                                            v
['Iface', 'Destination', 'Gateway', 'Flags', 'RefCnt', 'Use', 'Metric', 'Mask', 'MTU', 'Window','IRTT']
['wlp2s0', '00000000', '0101A8C0', '0003', '0', '0', '600', '00000000', '0', '0', '0']

'''
def scan_route():
    #routingData = []
    try:
        with open('/proc/net/route') as fdroute:
            routeData = fdroute.readlines()
    except IOError:
        routeData = ''
    for rd in routeData:
        route_Data = rd.rstrip().split()
        if route_Data[0] != 'Iface': # and route_Data[1] == '00000000' and route_Data[2] != '00000000':
            ifaceName = route_Data[0]
            x_ifaceDestination = route_Data[1]
            x_ifaceGateway = route_Data[2]
            x_ifaceMask = route_Data[7]
            
            x_ifaceGateANDMask = hex(int(x_ifaceDestination, 16) & int(x_ifaceMask, 16))
            x_ifaceNewWay = str(x_ifaceGateANDMask)[2:]
            x_ifaceNewWaylen = len(x_ifaceNewWay)
            if x_ifaceNewWaylen < 8:
                x_ifaceNewWay = '0' * (8-x_ifaceNewWaylen) + x_ifaceNewWay
            ifaceMaskBits = bin(int(x_ifaceMask, 16)).count('1')
            s_ifaceDestination = str(int(x_ifaceDestination[6:8], 16)) + '.' + \
            str(int(x_ifaceDestination[4:6], 16)) + '.' + \
            str(int(x_ifaceDestination[2:4], 16)) + '.' + \
            str(int(x_ifaceDestination[0:2], 16))
            s_ifaceGateway = str(int(x_ifaceGateway[6:8], 16)) + '.' + \
            str(int(x_ifaceGateway[4:6], 16)) + '.' + \
            str(int(x_ifaceGateway[2:4], 16)) + '.' + \
            str(int(x_ifaceGateway[0:2], 16))
            s_ifaceMask = str(int(x_ifaceMask[6:8], 16)) + '.' + \
            str(int(x_ifaceMask[4:6], 16)) + '.' + \
            str(int(x_ifaceMask[2:4], 16)) + '.' + \
            str(int(x_ifaceMask[0:2], 16))
            s_ifaceNewWay = str(int(x_ifaceNewWay[6:8], 16)) + '.' + \
            str(int(x_ifaceNewWay[4:6], 16)) + '.' + \
            str(int(x_ifaceNewWay[2:4], 16)) + '.' + \
            str(int(x_ifaceNewWay[0:2], 16))
            iface = {
                'IP': get_ip_address(ifaceName),
                'ifaceName': ifaceName,
                'network_hex': x_ifaceDestination,
                'network': s_ifaceDestination,
                'getway_hex': x_ifaceGateway,
                'gateway': s_ifaceGateway,
                'mask_hex': x_ifaceMask,
                'mask': s_ifaceMask,
                'mask_len': ifaceMaskBits, 
            }
            print ifaceName
            pprint(iface)
            #print '  Dest: ', x_ifaceDestination, ' Gateway: ', x_ifaceGateway, ' Mask: ', x_ifaceMask, ' AND: x:', x_ifaceGateANDMask, \
            #'b10', x_ifaceNewWay
            #print '  Dest: ', s_ifaceDestination, ' Gateway: ', s_ifaceGateway, ' Mask: ', s_ifaceMask, ' AND: ', s_ifaceNewWay


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
)[20:24])

def get_networkMask(ifname):
    return socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', 'usb0'))[20:24])

def get_struct(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24]

if __name__ == '__main__':
    scan_route()

