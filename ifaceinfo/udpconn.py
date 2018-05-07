import os
import sys
#import socket
#import fcntl
#import struct
import time
from pprint import pprint
from ifaceinfotools import Conn

class UDPConn(Conn):
    def __init__(self):
        Conn.__init__(self, '/proc/net/udp', 'udp')

    def refresh(self):
        '''
        this function refresh the informations collected when the class is loaded
        if you want to work with fresh data use this function to reload the data updated
        '''
        self.__init__()
    
    def reload(self):
        '''
        same as self.refresh()
        '''
        self.refresh()

class UDP6Conn(Conn):
    def __init__(self):
        Conn.__init__(self, '/proc/net/udp6', 'udp6')

    def refresh(self):
        '''
        this function refresh the informations collected when the class is loaded
        if you want to work with fresh data use this function to reload the data updated
        '''
        self.__init__()
    
    def reload(self):
        '''
        same as self.refresh()
        '''
        self.refresh()