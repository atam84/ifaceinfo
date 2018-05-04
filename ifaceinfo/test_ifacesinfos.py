#!/usr/bin/env python


import sys
from pprint import pprint

sys.path.append('./modules')
from ifaceinfo import InterfacesInfos


def iface_test():
    networkiface = InterfacesInfos()
    print('list all interfaces :')
    pprint(networkiface.ifaces_list())
    print('number of interfaces :')
    pprint(networkiface.ifaces_count())
    print('list interface with ifindex = 4, with full interface informations : ')
    pprint(networkiface.iface_by_ifindex(4))
    print('list interface with iflink = 6, with brief interface informations :')
    pprint(networkiface.iface_by_iflink('6', 'brief'))
    print('refresh network interfaces informations :')
    pprint(networkiface.refresh())
    print('list all interfaces informations :')
    pprint(networkiface.ifaces_info())
    print('list interface up with brief informations:')
    pprint(networkiface.ifaces_by_status('up', 'brief'))
    print('list interfaces info as dict :')
    pprint(networkiface.as_dict())
    print('list interfaces info as dict :')
    pprint(networkiface.list_interfaces())
    pprint(networkiface.iface_as_dict('usb0'))
    pprint(networkiface.ifaces_statistics_as_dict())
    print('list all interfaces type :')
    pprint(networkiface.ifaces_type())



if __name__ == '__main__':
    iface_test()