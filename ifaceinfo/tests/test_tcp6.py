#!/usr/bin/env python

import sys
sys.path.append('../')
from tcpconn import TCP6Conn
from pprint import pprint

tcp6 = TCP6Conn()

def tcp6conn_test():
    print('#### List all tcp6 connexion :')
    print('```py')
    pprint(tcp6.connexion())
    print('```')
    print('#### List connexion with listening state (0x0A) :')
    print('```py')
    pprint(tcp6.get_listen_conn())
    print('```')
    print('#### Remote address (incoming) : ')
    print('```py')
    pprint(tcp6.remote_addrs())
    print('```')
    print('#### Remote remote ports (outgoing) : ')
    print('```py')
    pprint(tcp6.remote_ports())
    print('```')
    print('#### Local address (outgoing conn) :')
    print('```py')
    pprint(tcp6.local_addrs())
    print('```')
    print('#### Local ports (incoming) :')
    print('```py')
    pprint(tcp6.local_ports())
    print('```')


if __name__ == '__main__':
    tcp6conn_test()
