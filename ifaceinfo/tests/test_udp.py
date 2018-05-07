#!/usr/bin/env python

import sys
sys.path.append('../')
from udpconn import UDPConn
from pprint import pprint

udp = UDPConn()

def udpconn_test():
    print('#### List all udp connexion :')
    print('```py')
    pprint(udp.connexion())
    print('```')
    print('#### List connexion with listening state (0x0A) :')
    print('```py')
    pprint(udp.get_listen_conn())
    print('```')
    print('#### Remote address (incoming) : ')
    print('```py')
    pprint(udp.remote_addrs())
    print('```')
    print('#### Remote remote ports (outgoing) : ')
    print('```py')
    pprint(udp.remote_ports())
    print('```')
    print('#### Local address (outgoing conn) :')
    print('```py')
    pprint(udp.local_addrs())
    print('```')
    print('#### Local ports (incoming) :')
    print('```py')
    pprint(udp.local_ports())
    print('```')


if __name__ == '__main__':
    udpconn_test()
