#!/usr/bin/env python

from ifaceinfo import TCPConn
from pprint import pprint

tcp = TCPConn()

def tcpconn_test():
    print('#### List all tcp connexion :')
    print('```py')
    pprint(tcp.connexion())
    print('```')
    print('#### List connexion with listening state (0x0A) :')
    print('```py')
    pprint(tcp.get_listen_conn())
    print('```')
    print('#### Remote address (incoming) : ')
    print('```py')
    pprint(tcp.remote_addrs())
    print('```')
    print('#### Remote remote ports (outgoing) : ')
    print('```py')
    pprint(tcp.remote_ports())
    print('```')
    print('#### Local address (outgoing conn) :')
    print('```py')
    pprint(tcp.local_addrs())
    print('```')
    print('#### Local ports (incoming) :')
    print('```py')
    pprint(tcp.local_ports())
    print('```')


if __name__ == '__main__':
    tcpconn_test()
