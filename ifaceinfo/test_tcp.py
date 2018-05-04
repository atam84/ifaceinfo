#!/usr/bin/env python

from tcpconn import TCPConn
from pprint import pprint

tcp = TCPConn()

def tcpconn_test():
    print('** List all tcp connexion :')
    pprint(tcp.connexion())
    print('** List connexion with listening state (0x0A) :')
    pprint(tcp.get_listen_conn())
    print('** Remote address and local ports : ')
    pprint(tcp.remote_addrs())
    pprint(tcp.remote_ports())
    print('** Local address and local ports :')
    pprint(tcp.local_addrs())
    pprint(tcp.local_ports())


if __name__ == '__main__':
    tcpconn_test()
