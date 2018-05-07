import os
import sys
import socket
import fcntl
import struct
import time


class FileReader:
    def read_file_as_table(self, filename):
        '''
        private method that read given file completly and return it as list of lines
        '''
        try:
            # python 2 & 3 compatibility
            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
            if sys.version_info.major == 3:
                fd = open(filename, 'r', encoding='latin1')
            else:
                fd = open(filename, 'r')
            filecontents = fd.readlines()
            try:
                fd.close()
            except Exception:
                pass
        except IOError:
            filecontents = ''
        if type(filecontents) is list:
            filecontents.pop(0)
        return filecontents

class IfaceInfoTools:
    def __init__(self):
        self.IfaceInfoTools_version = '0.0.1'

    def ip_address(self, ifacename):
        '''
        private methode
        get ip address of interface using socket interface
        '''
        try:
            addr = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0x8915, struct.pack('256s', ifacename.encode()))[20:24])
        except (IOError, UnicodeDecodeError):
            addr = ''
        return addr

    def network_mask(self, ifacename):
        '''
        private methode
        get net mask address of interface using socket interface
        '''
        try:
            mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifacename.encode()))[20:24])
        except (IOError, UnicodeDecodeError):
            mask = ''
        return mask

    def network_address(self, ipaddr, mask):
        '''
        private methode
        used to calculate the network address
        '''
        x_ip = self.ip2hex(ipaddr)
        x_mask = self.ip2hex(mask)
        return self.hex2ip(hex(int(x_ip, 16) & int(x_mask, 16)))

    def ip2hex(self, addr):
        '''
        private methode
        convert string decimal ip address to hexadecimal representation
        return string (as hex representation)
        '''
        addr = addr.split('.')
        if len(addr) == 4:
            return '{:02x}{:02x}{:02x}{:02x}'.format(int(addr[0]), int(addr[1]), int(addr[2]), int(addr[3]))
        else:
            return ''

    def hex2ip(self, x_addr):
        '''
        private methode
        convert hexadecimal representation to string decimal ip address
        return string (as ip address representation)
        '''
        addr = '{:08x}'.format(int(x_addr.replace('0x', ''), 16))
        if len(addr) == 8:
            return '{:d}.{:d}.{:d}.{:d}'.format(int(addr[0:2], 16), int(addr[2:4], 16), int(addr[4:6], 16), int(addr[6:8], 16))
        else:
            return ''

    def reverse_ip(self, ipaddress):
        '''
        Private method that reverse ip address
        '''
        _ipaddr = ipaddress.split('.')
        return '{}.{}.{}.{}'.format(_ipaddr[3], _ipaddr[2], _ipaddr[1], _ipaddr[0])


class Conn(IfaceInfoTools, FileReader):
    '''
    this class provide a quick interface to read /proc/net/tcp and give the informations about the current connexion to host
    
    https://www.kernel.org/doc/Documentation/networking/proc_net_tcp.txt
    
    /proc/net/tcp   <<-- Example -->>
    sl  local_address rem_address   st   tx_queue         rx_queue     tr      tm->when retrnsmt   uid  timeout inode                                                     
    0: 0100007F:0035 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 32059 1 0000000000000000 100 0 0 10 0                     
    1: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 44971 1 0000000000000000 100 0 0 10 0                     
    2: 0100007F:0277 00000000:0000 0A 00000000:00000000 00:00000000 00000000     0        0 24125 1 0000000000000000 100 0 0 10 0                     
    3: 0100007F:6989 00000000:0000 0A 00000000:00000000 00:00000000 00000000   122        0 26080 1 0000000000000000 100 0 0 10 0                     
    4: 00000000:14EB 00000000:0000 0A 00000000:00000000 00:00000000 00000000   102        0 25337 1 0000000000000000 100 0 0 10 0                     
    5: 2401A8C0:AC56 2401A8C0:0016 01 00000000:00000000 02:0007DDFA 00000000  1000        0 59815 3 0000000000000000 20 4 30 10 -1                    
    6: 2401A8C0:0016 2401A8C0:AC56 01 00000000:00000000 02:0007DDFA 00000000     0        0 61538 4 0000000000000000 20 4 31 10 17                    
    7: 2401A8C0:E71E CEC93AD8:01BB 01 00000000:00000000 00:00000000 00000000  1000        0 69532 1 0000000000000000 39 4 30 10 -1                    
    8: 2401A8C0:E360 8A13D9AC:01BB 01 00000000:00000000 00:00000000 00000000  1000        0 72008 1 0000000000000000 158 4 30 10 -1                   
    '''
    def __init__(self, procfilename, protocole):
        '''
        initialization method that inherit IfaceInfoTools class
        '''
        FileReader
        IfaceInfoTools
        self.__state = {
            '01': 'established',
            '02': 'syn_sent',
            '03': 'syn_recv',
            '04': 'fin_wait1',
            '05': 'fin_wait2',
            '06': 'time_wait',
            '07': 'close',
            '08': 'close_wait',
            '09': 'last_ack',
            '0A': 'listen',
            '0B': 'closing',
            '0C': 'max_states'
        }
        self.__timestamp = int(time.time())
        self.__connexion = self.__connexion_parser(procfilename, protocole)
        #self.tcp6_connexion = self.__tcp6_connexion_parser('/proc/net/tcp6')

    def __code_state(self, hexcode):
        '''
        private method that return the connexion status from the code of the connexion status (st)
        '''
        if hexcode in self.__state:
            return self.__state[hexcode]
        return 'unknwon'

    def __connexion_parser(self, filename, protocle):
        '''
        private function that parse the /proc/net/{tcp, udp} and give human readable ip, ports and status ...
        '''
        _connexion = []
        _jump = 4
        for _tcpconn in self.read_file_as_table(filename):
            _element = _tcpconn.split()
            _localaddr = _element[1].split(':')
            _remotraddr = _element[2].split(':')
            if protocle == 'tcp' or protocle == 'udp':
                _ip_local = self.reverse_ip(self.hex2ip(_localaddr[0]))
                _ip_remote = self.reverse_ip(self.hex2ip(_remotraddr[0]))
            elif protocle == 'tcp6' or protocle == 'udp6':
                _ip_local = ':'.join([_localaddr[0][i:i+_jump] for i in range(0, len(_localaddr[0]), _jump)])
                _ip_remote = ':'.join([_remotraddr[0][i:i+_jump] for i in range(0, len(_remotraddr[0]), _jump)])
            _connexion.append({
                'sl': _element[0].replace(':', ''),
                'local_address': {
                    'x_addr': _localaddr[0],
                    'x_port': _localaddr[1],
                    'ip': _ip_local,
                    'port': int(_localaddr[1], 16)
                },
                'rem_address': {
                    'x_addr': _remotraddr[0],
                    'x_port': _remotraddr[1],
                    'ip': _ip_remote,
                    'port': int(_remotraddr[1], 16)
                },
                'st': _element[3],
                'tx_queue': _element[4],
                'rx_queue': _element[5],
                'tr': _element[6],
                'tm->when': _element[7],
                'retrnsmt': _element[8],
                'uid': _element[9],
                'timeout': _element[10],
                'inode': _element[11],
                'protocole': protocle,
                'status': self.__code_state(_element[3])
            })
        return _connexion

    def connexion(self):
        '''
        return a list of all {tcp, udp} connexion
        '''
        return self.__connexion

    def conn(self):
        '''
        (alias) same is connexion(self)
        '''
        return self.connexion()

    def conn_by_status(self, connstatus):
        '''
        get {tcp, udp} connexion with last_ack '09' {tcp, udp} status
        '''
        _connstatus = connstatus.replace('0x', '')
        __statusconn = []
        for __conn in self.connexion():
            if __conn['st'] == _connstatus or __conn['status'] == _connstatus:
                __statusconn.append(__conn)
        return __statusconn

    def get_established_conn(self):
        '''
        get {tcp, udp} connexion with established '01' {tcp, udp} status
        '''
        return self.conn_by_status('0x01')

    def get_syn_sent_conn(self):
        '''
        get {tcp, udp} connexion with syn_sent '02' {tcp, udp} status
        '''
        return self.conn_by_status('0x02')

    def get_syn_recv_conn(self):
        '''
        get {tcp, udp} connexion with recv '03' {tcp, udp} status
        '''
        return self.conn_by_status('0x03')

    def get_fin_wait1_conn(self):
        '''
        get {tcp, udp} connexion with fin_wait1 '04' {tcp, udp} status
        '''
        return self.conn_by_status('0x04')

    def get_fin_wait2_conn(self):
        '''
        get {tcp, udp} connexion with fin_wait2 '05' {tcp, udp} status
        '''
        return self.conn_by_status('0x05')

    def get_time_wait_conn(self):
        '''
        get {tcp, udp} connexion with time_wait '06' {tcp, udp} status
        '''
        return self.conn_by_status('0x06')

    def get_close_conn(self):
        '''
        get {tcp, udp} connexion with close '07' {tcp, udp} status
        '''
        return self.conn_by_status('0x07')

    def get_close_wait_conn(self):
        return self.conn_by_status('0x08')

    def get_last_ack_conn(self):
        '''
        get {tcp, udp} connexion with last_ack '09' {tcp, udp} status
        '''
        return self.conn_by_status('0x09')

    def get_listen_conn(self):
        '''
        get {tcp, udp} connexion with listen '0A' {tcp, udp} status
        '''
        return self.conn_by_status('0x0A')

    def get_closing_conn(self):
        '''
        get {tcp, udp} connexion with closing '0B' {tcp, udp} status
        '''
        return self.conn_by_status('0x0B')

    def get_max_state_conn(self):
        '''
        get {tcp, udp} connexion with max_state '0C' {tcp, udp} status
        '''
        return self.conn_by_status('0x0C')

    def __get_conn_data(self, what='port', scope='local', value=0):
        '''
        this private function is not used
        '''
        _conn = []
        if scope == 'local':
            _scope = 'local_address'
        elif scope == 'remote':
            _scope = 'rem_address'
        elif scope == 'none':
            _scope = 'none'
        if _scope == 'none':
            for _conn in self.connexion():
                if _conn[what] == value:
                    _conn.append(_conn)
        else:
            for _conn in self.connexion():
                if _conn[scope][what] == value:
                    _conn.append(_conn)
        return _conn

    def remote_ports(self):
        '''
        get list of ports used by remote host
        '''
        _ports = []
        for _conn in self.connexion():
            _ports.append(_conn['rem_address']['port'])
        return list(set(_ports))

    def local_ports(self):
        '''
        get list of ports used by local host [listen, established, ...]
        '''
        _ports = []
        for _conn in self.connexion():
            _ports.append(_conn['local_address']['port'])
        return list(set(_ports))

    def remote_addrs(self):
        '''
        get dict of remote address and ports list
        {
            'remote_host_ip': [list of ports],
        }
        '''
        _addrs = {}
        for _conn in self.connexion():
            if _conn['rem_address']['ip'] not in _addrs:
                _addrs[_conn['rem_address']['ip']] = []
            if _conn['rem_address']['port'] not in _addrs[_conn['rem_address']['ip']]:
                _addrs[_conn['rem_address']['ip']].append(_conn['rem_address']['port'])
        return _addrs

    def local_addrs(self):
        '''
        get dict of local address and ports list
        {
            'local_host_ip': [list of ports]
        }
        '''
        _addrs = {}
        for _conn in self.connexion():
            if _conn['local_address']['ip'] not in _addrs:
                _addrs[_conn['local_address']['ip']] = []
            if _conn['local_address']['port'] not in _addrs[_conn['local_address']['ip']]:
                _addrs[_conn['local_address']['ip']].append(_conn['local_address']['port'])
        return _addrs


