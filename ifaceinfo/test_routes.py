#!/usr/bin/env python


import sys
from pprint import pprint

sys.path.append('./modules')
from ifaceinfo import InterfacesInfos


def route_test():
    networkiface = InterfacesInfos()
    print('list routing table for all interfaces :')
    pprint(networkiface.ifaces_routes())


if __name__ == '__main__':
    route_test()
