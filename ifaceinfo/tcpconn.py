import os
import sys
#import socket
#import fcntl
#import struct
import time
from pprint import pprint
from ifaceinfotools import Conn

class TCPConn(Conn):
    def __init__(self):
        Conn.__init__(self, '/proc/net/tcp', 'tcp')

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

class TCP6Conn(Conn):
    def __init__(self):
        Conn.__init__(self, '/proc/net/tcp6', 'tcp6')

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

#class TCPConn(IfaceInfoTools):
#    '''
#    this class provide a quick interface to read /proc/net/tcp and give the informations about the current connexion to host
#    
#    https://www.kernel.org/doc/Documentation/networking/proc_net_tcp.txt
#    
#    /proc/net/tcp   <<-- Example -->>
#    sl  local_address rem_address   st   tx_queue         rx_queue     tr      tm->when retrnsmt   uid  timeout inode                                                     
#    0: 0100007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 32059 1 0000000000000000 100 0 0 10 0                     
#    1: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 44971 1 0000000000000000 100 0 0 10 0                     
#    2: 0100007F:0277 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 24125 1 0000000000000000 100 0 0 10 0                     
#    3: 0100007F:6989 00000000:0000 0A 00000000:00000000 00:00000000 00000000   122        0 26080 1 0000000000000000 100 0 0 10 0                     
#    4: 00000000:14EB 00000000:0000 0A 00000000:00000000 00:00000000 00000000   102        0 25337 1 0000000000000000 100 0 0 10 0                     
#    5: 2401A8C0:AC56 2401A8C0:0016 01 00000000:00000000 02:0007DDFA 00000000  1000        0 59815 3 0000000000000000 20 4 30 10 -1                    
#    6: 2401A8C0:0016 2401A8C0:AC56 01 00000000:00000000 02:0007DDFA 00000000     0        0 61538 4 0000000000000000 20 4 31 10 17                    
#    7: 2401A8C0:E71E CEC93AD8:01BB 01 00000000:00000000 00:00000000 00000000  1000        0 69532 1 0000000000000000 39 4 30 10 -1                    
#    8: 2401A8C0:E360 8A13D9AC:01BB 01 00000000:00000000 00:00000000 00000000  1000        0 72008 1 0000000000000000 158 4 30 10 -1                   
#    '''
#    def __init__(self):
#        '''
#        initialization method that inherit IfaceInfoTools class
#        '''
#        IfaceInfoTools
#        self.__tcpstate = {
#            '01': 'established',
#            '02': 'syn_sent',
#            '03': 'syn_recv',
#            '04': 'fin_wait1',
#            '05': 'fin_wait2',
#            '06': 'time_wait',
#            '07': 'close',
#            '08': 'close_wait',
#            '09': 'last_ack',
#            '0A': 'listen',
#            '0B': 'closing',
#            '0C': 'max_states'
#        }
#        self.__timestamp = int(time.time())
#        self.__tcp_connexion = self.__tcp_connexion_parser('/proc/net/tcp', 'tcp')
#        #self.tcp6_connexion = self.__tcp6_connexion_parser('/proc/net/tcp6')
#
#    def __code_tcpstate(self, hexcode):
#        '''
#        private method that return the connexion status from the code of the connexion status (st)
#        '''
#        if hexcode in self.__tcpstate:
#            return self.__tcpstate[hexcode]
#        return 'unknwon'
#
#    def __read_file_as_table(self, filename):
#        '''
#        private method that read given file completly and return it as list of lines
#        '''
#        try:
#            # python 2 & 3 compatibility
#            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
#            if sys.version_info.major == 3:
#                fd = open(filename, 'r', encoding='latin1')
#            else:
#                fd = open(filename, 'r')
#            filecontents = fd.readlines()
#            try:
#                fd.close()
#            except Exception:
#                pass
#        except IOError:
#            filecontents = False
#        if type(filecontents) is list:
#            filecontents.pop(0)
#        return filecontents
#
#    def __tcp_connexion_parser(self, filename, protocle):
#        '''
#        private function that parse the /proc/net/tcp and give human readable ip, ports and status ...
#        '''
#        _tcpconnexion = []
#        for _tcpconn in self.__read_file_as_table(filename):
#            _element = _tcpconn.split()
#            _localaddr = _element[1].split(':')
#            _remotraddr = _element[2].split(':')
#            _tcpconnexion.append({
#                'sl': _element[0].replace(':', ''),
#                'local_address': {
#                    'x_addr': _localaddr[0],
#                    'x_port': _localaddr[1],
#                    'ip': self.reverse_ip(self.hex2ip(_localaddr[0])),
#                    'port': int(_localaddr[1], 16)
#                },
#                'rem_address': {
#                    'x_addr': _remotraddr[0],
#                    'x_port': _remotraddr[1],
#                    'ip': self.reverse_ip(self.hex2ip(_remotraddr[0])),
#                    'port': int(_remotraddr[1], 16)
#                },
#                'st': _element[3],
#                'tx_queue': _element[4],
#                'rx_queue': _element[5],
#                'tr': _element[6],
#                'tm->when': _element[7],
#                'retrnsmt': _element[8],
#                'uid': _element[9],
#                'timeout': _element[10],
#                'inode': _element[11],
#                'protocole': protocle,
#                'status': self.__code_tcpstate(_element[3])
#            })
#        return _tcpconnexion
#
#    def refresh(self):
#        '''
#        this function refresh the informations collected when the class is loaded
#        if you want to work with fresh data use this function to reload the data updated
#        '''
#        self.__init__()
#    
#    def reload(self):
#        '''
#        same as self.refresh()
#        '''
#        self.refresh()
#
#    def tcp_connexion(self):
#        '''
#        return a list of all tcp connexion
#        '''
#        return self.__tcp_connexion
#
#    def tcp_conn(self):
#        '''
#        (alias) same is tcp_connexion(self)
#        '''
#        return self.tcp_connexion()
#
#    def conn_by_status(self, connstatus):
#        '''
#        get tcp connexion with last_ack '09' tcp status
#        '''
#        _connstatus = connstatus.replace('0x', '')
#        _tcpconn = []
#        for __conn in self.tcp_connexion():
#            if __conn['st'] == _connstatus or __conn['status'] == _connstatus:
#                _tcpconn.append(__conn)
#        return _tcpconn
#
#    def get_established_tcp_conn(self):
#        '''
#        get tcp connexion with established '01' tcp status
#        '''
#        return self.conn_by_status('0x01')
#
#    def get_syn_sent_tcp_conn(self):
#        '''
#        get tcp connexion with syn_sent '02' tcp status
#        '''
#        return self.conn_by_status('0x02')
#
#    def get_syn_recv_tcp_conn(self):
#        '''
#        get tcp connexion with recv '03' tcp status
#        '''
#        return self.conn_by_status('0x03')
#
#    def get_fin_wait1_tcp_conn(self):
#        '''
#        get tcp connexion with fin_wait1 '04' tcp status
#        '''
#        return self.conn_by_status('0x04')
#
#    def get_fin_wait2_tcp_conn(self):
#        '''
#        get tcp connexion with fin_wait2 '05' tcp status
#        '''
#        return self.conn_by_status('0x05')
#
#    def get_time_wait_tcp_conn(self):
#        '''
#        get tcp connexion with time_wait '06' tcp status
#        '''
#        return self.conn_by_status('0x06')
#
#    def get_close_tcp_conn(self):
#        '''
#        get tcp connexion with close '07' tcp status
#        '''
#        return self.conn_by_status('0x07')
#
#    def get_close_wait_tcp_conn(self):
#        return self.conn_by_status('0x08')
#
#    def get_last_ack_tcp_conn(self):
#        '''
#        get tcp connexion with last_ack '09' tcp status
#        '''
#        return self.conn_by_status('0x09')
#
#    def get_listen_tcp_conn(self):
#        '''
#        get tcp connexion with listen '0A' tcp status
#        '''
#        return self.conn_by_status('0x0A')
#
#    def get_closing_tcp_conn(self):
#        '''
#        get tcp connexion with closing '0B' tcp status
#        '''
#        return self.conn_by_status('0x0B')
#
#    def get_max_state_tcp_conn(self):
#        '''
#        get tcp connexion with max_state '0C' tcp status
#        '''
#        return self.conn_by_status('0x0C')
#
#    def __get_conn_data(self, what='port', scope='local', value=0):
#        '''
#        this private function is not used
#        '''
#        _tcpconn = []
#        if scope == 'local':
#            _scope = 'local_address'
#        elif scope == 'remote':
#            _scope = 'rem_address'
#        elif scope == 'none':
#            _scope = 'none'
#        if _scope == 'none':
#            for _conn in self.tcp_connexion():
#                if _conn[what] == value:
#                    _tcpconn.append(_conn)
#        else:
#            for _conn in self.tcp_connexion():
#                if _conn[scope][what] == value:
#                    _tcpconn.append(_conn)
#        return _tcpconn
#
#    def remote_ports(self):
#        '''
#        get list of ports used by remote host
#        '''
#        _ports = []
#        for _conn in self.tcp_connexion():
#            _ports.append(_conn['rem_address']['port'])
#        return list(set(_ports))
#
#    def local_ports(self):
#        '''
#        get list of ports used by local host [listen, established, ...]
#        '''
#        _ports = []
#        for _conn in self.tcp_connexion():
#            _ports.append(_conn['local_address']['port'])
#        return list(set(_ports))
#
#    def remote_addrs(self):
#        '''
#        get dict of remote address and ports list
#        {
#            'remote_host_ip': [list of ports],
#        }
#        '''
#        _addrs = {}
#        for _conn in self.tcp_connexion():
#            if _conn['rem_address']['ip'] not in _addrs:
#                _addrs[_conn['rem_address']['ip']] = []
#            if _conn['rem_address']['port'] not in _addrs[_conn['rem_address']['ip']]:
#                _addrs[_conn['rem_address']['ip']].append(_conn['rem_address']['port'])
#        return _addrs
#
#    def local_addrs(self):
#        '''
#        get dict of local address and ports list
#        {
#            'local_host_ip': [list of ports]
#        }
#        '''
#        _addrs = {}
#        for _conn in self.tcp_connexion():
#            if _conn['local_address']['ip'] not in _addrs:
#                _addrs[_conn['local_address']['ip']] = []
#            if _conn['local_address']['port'] not in _addrs[_conn['local_address']['ip']]:
#                _addrs[_conn['local_address']['ip']].append(_conn['local_address']['port'])
#        return _addrs
#
#
#