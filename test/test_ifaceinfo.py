#!/usr/bin/env python


import sys
from pprint import pprint

sys.path.append('./modules')
from ifaceinfo import networkInterfaceInfo


def iface_test():
    networkiface = networkInterfaceInfo()
    #pprint(networkiface.ifacesList())
    #pprint(networkiface.ifacesCount())
    #pprint(networkiface.getifaceInfo('wlp2s0'))
    #pprint(networkiface.getifacesLink())
    #pprint(networkiface.getifacesIndex())
    #pprint(networkiface.getifacesIndexLink())
    pprint(networkiface.getifaceByIndex(4))
    pprint(networkiface.getifaceByLink('6', 'brief'))
    pprint(networkiface.refresh())
    pprint(networkiface.getifacesInfo())
    #pprint(networkiface.getifacesByStatus('up', 'full'))


if __name__ == '__main__':
    iface_test()
