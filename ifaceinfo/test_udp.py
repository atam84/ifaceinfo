#!/usr/bin/env python

from udpconn import UDPConn
from pprint import pprint

udp = UDPConn()

def udpconn_test():
    print('** List all udp connexion :')
    pprint(udp.connexion())
    print('** List connexion with listening state (0x0A) :')
    pprint(udp.get_listen_conn())
    print('** Remote address and local ports : ')
    pprint(udp.remote_addrs())
    pprint(udp.remote_ports())
    print('** Local address and local ports :')
    pprint(udp.local_addrs())
    pprint(udp.local_ports())


if __name__ == '__main__':
    udpconn_test()
