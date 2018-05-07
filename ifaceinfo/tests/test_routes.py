#!/usr/bin/env python


#import sys
#from pprint import pprint
#sys.path.append('./modules')
#from ifaceinfo import InterfacesInfos
from ifaceinfo import InterfacesRoutes
from pprint import pprint

def route_test():
    ifaceroutes = InterfacesRoutes()
    print('list routing table for all interfaces :')
    pprint(ifaceroutes.ifaces_routes())


if __name__ == '__main__':
    route_test()
