import os
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
        self.ifacesInfo = self.getIfaceInfo('/sys/class/net')

    def refresh(self):
        self.__init__()
    
    def reload(self):
        self.__init__()

    def getIfaceInfo(self, path):
        objArray = []
        ''' check if the path is directory and you have read access '''
        if not os.path.isdir(path) or not os.access(path, os.R_OK):
            raise Exception('Error: you are not allowed')
        ''' let get the elements in this first level directory '''
        try:
            netInterfaces = os.listdir(path)
        except Exception as err:
            raise Exception('Error: Cannot read the main directory')
        ''' let collect network interfaces '''
        for iface in netInterfaces:
            netIface = {}
            if os.path.isdir(os.path.join(path, iface)):
                ''' create the interface object and begin the data collection '''
                netIface['name'] = iface
                netIface['ip'] = self.get_ipAddress(iface)
                netIface['mask'] = self.get_networkMask(iface)
                netIfaceDir = os.path.join(path, iface)
                ''' get the interface params '''
                try:
                    netIfaceParams = os.listdir(netIfaceDir)
                except IOError as IOE:
                    pass
                for param in netIfaceParams:
                    if os.path.isfile(os.path.join(netIfaceDir, param)):
                        ''' here we read every param file and we put the data collected on the  '''
                        try:
                            with open(os.path.join(netIfaceDir, param)) as fd:
                                paramValue = fd.read()
                        except IOError as IOE:
                            paramValue = ''
                        netIface[param] = paramValue.rstrip()
                        fd.close()
                    if os.path.isdir(os.path.join(netIfaceDir, param)):
                        netIface[param] = self.scan_object(os.path.join(netIfaceDir, param), param)
                objArray.append(netIface)
        return objArray

    def scan_object(self, path, object_name):
        scan_obj = {}
        try:
            sub_objects = os.listdir(path)
        except IOError as IOE:
            pass
        for sub_object in sub_objects:
            if os.path.isfile(os.path.join(path, sub_object)):
                try:
                    __fd = open(os.path.join(path, sub_object), "r")
                    paramValue = __fd.read()
                    __fd.close()
                except IOError as IOE:
                    paramValue = ''
                scan_obj[sub_object] = paramValue.rstrip()
            #if os.path.isdir(os.path.join(path, sub_object)):
                #scan_obj[sub_object] = scan_object(os.path.join(path, sub_object), sub_object)
                #print 'Dir: ' + path + '/' + sub_object, sub_object
        return scan_obj

    def ifacesCount(self):
        return len(self.ifacesInfo)

    def ifacesList(self):
        iface_lst = []
        for iface in self.ifacesInfo:
            iface_lst.append(iface['name'])
        return iface_lst
    
    def getifaceInfo(self, ifaceName):
        for iface in self.ifacesInfo:
            if iface['name'] == ifaceName:
                return iface
        return {}

    def getifacesInfo(self):
        return self.ifacesInfo

    def getifacesIndex(self):
        ifacesIndex = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['ifindex'] = iface['ifindex']
            ifacesIndex.append(_iface)
        return ifacesIndex

    def getifacesLink(self):
        ifacesLink = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['iflink'] = iface['iflink']
            ifacesLink.append(_iface)
        return ifacesLink

    def getifacesIndexLink(self):
        ifaceIndexLink = []
        for iface in self.ifacesInfo:
            _iface = {}
            _iface['name'] = iface['name']
            _iface['ifindex'] = iface['ifindex']
            _iface['iflink'] = iface['iflink']
            ifaceIndexLink.append(_iface)
        return ifaceIndexLink

    def getifaceByInterfaceUID(self, identifier, value, info='full'):
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
                    elif info == 'full':
                        _iface = iface
                    _ifaceIndex.append(_iface)
            except Exception:
                pass
        return _ifaceIndex
    
    def getifaceByIndex(self, index, info='full'):
        return self.getifaceByInterfaceUID('ifindex', index, info)

    def getifaceByLink(self, link, info='full'):
        return self.getifaceByInterfaceUID('iflink', link, info)

    def getifacesByStatus(self, status, info='full'):
        _ifaces = []
        for iface in self.ifacesInfo:
            try:
                if iface['operstate'] == status:
                    if info == 'brief':
                        _iface = {}
                        _iface['name'] = iface['name']
                        _iface['ifindex'] = iface['ifindex']
                        _iface['iflink'] = iface['iflink']
                    elif info == 'full':
                        _iface = iface
                    _ifaces.append(_iface)
            except Exception:
                pass
        return _ifaces

    def getifacesUp(self, info='full'):
        return self.getifacesByStatus('up', info)

    def getifacesDown(self, info='full'):
        return self.getifacesByStatus('down', info)

    #def get_ip_address(ifname):
    #    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

    def get_ipAddress(self, ifaceName):
        try:
            addr = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0x8915, struct.pack('256s', ifaceName))[20:24])
        except IOError:
            addr = ''
        return addr

    def get_networkMask(self, ifaceName):
        try:
            mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', ifaceName))[20:24])
        except IOError:
            mask = ''
        return mask



