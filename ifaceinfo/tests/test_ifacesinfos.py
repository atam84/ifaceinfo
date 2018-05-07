#!/usr/bin/env python


import sys
from pprint import pprint

sys.path.append('./modules')
from ifaceinfo import InterfacesInfos


def iface_test():
    networkiface = InterfacesInfos()
    print('#### list all interfaces :')
    print('```py')
    pprint(networkiface.ifaces_list())
    print('```')
    print('#### number of interfaces :')
    print('```py')
    pprint(networkiface.ifaces_count())
    print('```')
    print('#### list interface with ifindex = 4, with full interface informations : ')
    print('```py')
    pprint(networkiface.iface_by_ifindex(4))
    print('```')
    print('#### list interface with iflink = 6, with brief interface informations :')
    print('```py')
    pprint(networkiface.iface_by_iflink('6', 'brief'))
    print('```')
    print('#### refresh network interfaces informations :')
    print('```py')
    pprint(networkiface.refresh())
    print('```')
    print('#### list all interfaces informations :')
    print('```py')
    pprint(networkiface.ifaces_info())
    print('```')
    print('#### list interface up with brief informations:')
    print('```py')
    pprint(networkiface.ifaces_by_status('up', 'brief'))
    print('```')
    print('#### list interfaces info as dict :')
    print('```py')
    pprint(networkiface.as_dict())
    print('```')
    print('#### list interfaces info as dict :')
    print('```py')
    pprint(networkiface.list_interfaces())
    print('```')
    print('#### get information about usb0 used as network interface')
    print('```py')
    pprint(networkiface.iface_as_dict('usb0'))
    print('```')
    print('#### get statistics of all interfaces as dict:')
    print('```py')
    pprint(networkiface.ifaces_statistics_as_dict())
    print('```')
    print('#### list all interfaces type :')
    print('```py')
    pprint(networkiface.ifaces_type())
    print('```')



if __name__ == '__main__':
    iface_test()
