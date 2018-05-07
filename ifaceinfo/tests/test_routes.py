#!/usr/bin/env python


import sys
sys.path.append('../')
#from ifaceinfo import InterfacesRoutes
from ifaceroutes import InterfacesRoutes
from pprint import pprint

def route_test():
    ifaceroutes = InterfacesRoutes()
    print('list routing table for all interfaces :')
    pprint(ifaceroutes.ifaces_routes())


if __name__ == '__main__':
    route_test()
