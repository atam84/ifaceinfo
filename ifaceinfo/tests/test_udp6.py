#!/usr/bin/env python

import sys
sys.path.append('../')
from udpconn import UDP6Conn
from pprint import pprint

udp6 = UDP6Conn()

def udp6conn_test():
    print('#### List all udp6 connexion :')
    print('```py')
    pprint(udp6.connexion())
    print('```')
    print('#### List connexion with listening state (0x0A) :')
    print('```py')
    pprint(udp6.get_listen_conn())
    print('```')
    print('#### Remote address (incoming) : ')
    print('```py')
    pprint(udp6.remote_addrs())
    print('```')
    print('#### Remote remote ports (outgoing) : ')
    print('```py')
    pprint(udp6.remote_ports())
    print('```')
    print('#### Local address (outgoing conn) :')
    print('```py')
    pprint(udp6.local_addrs())
    print('```')
    print('#### Local ports (incoming) :')
    print('```py')
    pprint(udp6.local_ports())
    print('```')


if __name__ == '__main__':
    udp6conn_test()
