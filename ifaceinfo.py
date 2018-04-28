import os
import sys
import socket
import fcntl
import struct
from pprint import pprint

'''
this class operate using the files bellow
    - /sys/class/net/*/
    - /proc/net/route
    - /proc/net/tcp
    - /proc/net/udp
'''

class networkInterfaceInfo:
    def __init__(self):
        '''
        data initialisation
        maybe in the future somme other data will be loaded directly to improve performance and data usability
        '''
        self.version = '0.0.5'
        self.py_compatibility='2 and 3'
        self.ifacesInfo = self.getIfaceInfo('/sys/class/net')

    def refresh(self):
        '''
        this function refresh the informations collected when the class is loaded
        if you want to work with fresh data use the function to reload the data updated
        '''
        self.__init__()
    
    def reload(self):
        '''
        same as self.refresh()
        '''
        self.__init__()

    def getIfaceInfo(self, path):
        '''
        the main function that scan /sys/class/net to collect interfaces informations
        '''
        objArray = []
        ''' check if the path is directory and you have read access '''
        if not os.path.isdir(path) or not os.access(path, os.R_OK):
            raise Exception('Error: you are not allowed')
        ''' let get the elements in this first level directory '''
        try:
            netInterfaces = os.listdir(path)
        except Exception as Err:
            raise Exception('Error: Cannot read the main directory - ', Err)
        ''' let collect network interfaces '''
        for iface in netInterfaces:
            netIface = {}
            if os.path.isdir(os.path.join(path, iface)):
                ''' create the interface object and begin the data collection '''
                netIface['name'] = iface
                netIface['ip'] = self.get_ipAddress(iface)
                netIface['mask'] = self.get_networkMask(iface)
                if netIface['ip'] != '' and netIface['mask'] != '':
                    netIface['network_address'] = self.get_networkAddress(netIface['ip'], netIface['mask'])
                else:
                    netIface['network_address'] = ''
                netIfaceDir = os.path.join(path, iface)
                ''' get the interface params '''
                try:
                    netIfaceParams = os.listdir(netIfaceDir)
                except IOError:
                    pass
                for param in netIfaceParams:
                    if os.path.isfile(os.path.join(netIfaceDir, param)):
                        ''' here we read every param file and we put the data collected on the  '''
                        try:
                            '''
                            python 2 & 3 compatibility
                            UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
                            '''
                            if sys.version_info.major == 3:
                                fd = open(os.path.join(netIfaceDir, param), 'r', encoding='latin1')
                            else:
                                fd = open(os.path.join(netIfaceDir, param), 'r')
                            paramValue = fd.read()
                        except IOError:
                            paramValue = ''
                        fd.close()
                        netIface[param] = paramValue.rstrip()
                    if os.path.isdir(os.path.join(netIfaceDir, param)):
                        netIface[param] = self.scan_object(os.path.join(netIfaceDir, param), param)
                objArray.append(netIface)
        return objArray

    def scan_object(self, path, object_name):
        '''
        function used to scan the first level of sub directories in /sys/class/net/<iface>/
        '''
        scan_obj = {}
        try:
            sub_objects = os.listdir(path)
        except IOError:
            pass
        for sub_object in sub_objects:
            if os.path.isfile(os.path.join(path, sub_object)):
                try:
                    '''
                    python 2 & 3 compatibility
                    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
                    '''
                    if sys.version_info.major == 3:
                        __fd = open(os.path.join(path, sub_object), 'r', encoding='latin1')
                    else:
                        __fd = open(os.path.join(path, sub_object), 'r')
                    paramValue = __fd.readlines()
                except IOError:
                    paramValue = ''
                __fd.close()
                if len(paramValue) == 1:
                    scan_obj[sub_object] = paramValue[0].rstrip()
                else:
                    scan_obj[sub_object] = []
                    for val in paramValue:
                        scan_obj[sub_object].append(val.rstrip())
            #if os.path.isdir(os.path.join(path, sub_object)):
                #scan_obj[sub_object] = scan_object(os.path.join(path, sub_object), sub_object)
                #print 'Dir: ' + path + '/' + sub_object, sub_object
        return scan_obj

    def ifacesCount(self):
        '''
        return a number of detected interfaces
        '''
        return len(self.ifacesInfo)

    def ifacesList(self):
        '''
        get a list of interface name
        return array of string
        '''
        iface_lst = []
        for iface in self.ifacesInfo:
            iface_lst.append(iface['name'])
        return iface_lst
    
    def getifaceInfo(self, ifaceName):
        '''
        get specific interface name with full information
        return dict
        '''
        for iface in self.ifacesInfo:
            if iface['name'] == ifaceName:
                return iface
        return {}

    def getifacesInfo(self):
        '''
        get all interfaces informations (full collected information)
        '''
        return self.ifacesInfo

    def getifacesIndex(self):
        '''
        get all interfaces name and ifindex
        return array of dict
        '''
        ifacesIndex = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['ifindex'] = iface['ifindex']
            ifacesIndex.append(_iface)
        return ifacesIndex

    def getifacesLink(self):
        '''
        get all interfaces name and iflink
        return array of dict
        '''
        ifacesLink = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['iflink'] = iface['iflink']
            ifacesLink.append(_iface)
        return ifacesLink

    def getifacesIndexLink(self):
        '''
        get all interfaces with brief informations (name, ifindex, iflink, ip and mask)
        return an array of dict
        '''
        ifaceIndexLink = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['ifindex'] = iface['ifindex']
            _iface['iflink'] = iface['iflink']
            _iface['ip'] = iface['ip']
            _iface['mask'] = iface['mask']
            ifaceIndexLink.append(_iface)
        return ifaceIndexLink

    def getifaceByInterfaceUID(self, identifier, value, info='full'):
        '''
        get interfaces by defined identifier and value, the third parametre info allow 
        the choise to return the result as a full data or briefly
        
        the identifier can be any key value of the class definition
        this funtion is used by self.getifaceByIndex() and self.getifaceByLink()

        return an array of dict
        '''
        _ifaceIndex = []
        _value = str(value)
        for iface in self.ifacesInfo:
            try:
                if iface[identifier] == _value:
                    if info == 'brief':
                        _iface = {}
                        _iface['name'] = iface['name']
                        _iface['ifindex'] = iface['ifindex']
                        _iface['iflink'] = iface['iflink']
                        _iface['ip'] = iface['ip']
                        _iface['mask'] = iface['mask']
                    elif info == 'full':
                        _iface = iface
                    _ifaceIndex.append(_iface)
            except Exception:
                pass
        return _ifaceIndex
    
    def getifaceByIndex(self, ifindex, info='full'):
        '''
        get interface that have ifindex=X
        ifindex is located in /sys/class/net/<iface>/ifindex
        return an array with dict
        '''
        return self.getifaceByInterfaceUID('ifindex', ifindex, info)

    def getifaceByLink(self, iflink, info='full'):
        '''
        get interface that have iflink=X
        ifindex is located in /sys/class/net/<iface>/iflink
        return an array with dict
        '''
        return self.getifaceByInterfaceUID('iflink', iflink, info)

    def getifacesByStatus(self, status, info='full'):
        '''
        get interface by status, this function is used by self.getifacesUp() and self.getifacesDown()
        return an array with dict
        '''
        _ifaces = []
        for iface in self.ifacesInfo:
            try:
                if iface['operstate'] == status:
                    if info == 'brief':
                        _iface = {}
                        _iface['name'] = iface['name']
                        _iface['ifindex'] = iface['ifindex']
                        _iface['iflink'] = iface['iflink']
                        _iface['ip'] = iface['ip']
                        _iface['mask'] = iface['mask']
                    elif info == 'full':
                        _iface = iface
                    _ifaces.append(_iface)
            except Exception:
                pass
        return _ifaces

    def getifacesUp(self, info='full'):
        '''
        get interface up only
        return an array with dict
        '''
        return self.getifacesByStatus('up', info)

    def getifacesDown(self, info='full'):
        '''
        get interface down and other status
        return an array with dict
        '''
        return self.getifacesByStatus('down', info)

    #def get_ip_address(ifname):
    #    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

    def get_ipAddress(self, ifaceName):
        '''
        get ip address of interface using socket interface
        '''
        try:
            addr = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0x8915, struct.pack('256s', ifaceName.encode()))[20:24])
        except (IOError, UnicodeDecodeError):
            addr = ''
        return addr

    def get_networkMask(self, ifaceName):
        '''
        get net mask address of interface using socket interface
        '''
        try:
            mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifaceName.encode()))[20:24])
        except (IOError, UnicodeDecodeError):
            mask = ''
        return mask

    def get_networkAddress(self, ipaddr, mask):
        x_ip = self.ip2hex(ipaddr)
        x_mask = self.ip2hex(mask)
        return self.hex2ip(hex(int(x_ip, 16) & int(x_mask, 16)))

    def ip2hex(self, addr):
        '''
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
        convert hexadecimal representation to string decimal ip address
        return string (as ip address representation)
        '''
        addr = '{:08x}'.format(int(x_addr.replace('0x', ''), 16))
        if len(addr) == 8:
            return '{:d}.{:d}.{:d}.{:d}'.format(int(addr[0:2], 16), int(addr[2:4], 16), int(addr[4:6], 16), int(addr[6:8], 16))
        else:
            return ''

