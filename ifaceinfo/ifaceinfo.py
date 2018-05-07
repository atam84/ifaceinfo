import os
import sys
import socket
import fcntl
import struct
import time
from pprint import pprint
from ifaceinfotools import IfaceInfoTools

"""
this class operate using the files bellow
    - /sys/class/net/*/
    - /proc/net/route
    - /proc/net/tcp
    - /proc/net/udp
"""

class InterfacesInfos(IfaceInfoTools):
    def __init__(self):
        """
        data initialisation
        maybe in the future somme other data will be loaded directly to improve performance and data usability
        at this time the scan of /sys/class/net are performed in the initialisation of the class
        """
        IfaceInfoTools
        self.version = '0.1.7'
        self.github_url = 'https://github.com/atam84/ifaceinfo'
        self.__timestamp = self.timestamp = int(time.time())
        self.__ifaces_info = self.__get_ifaces_info('/sys/class/net')
        self.__ifaces_routes = self.__get_routes('/proc/net/route')
        self.__ifaces_infos__ = self.__set_as_dict(self.ifaces_info())

    ####################
    # Private Methodes
    ####################
    def __set_timestamp(self):
        return int(time.time())

    def __set_as_dict(self, iface):
        """
        Private method that convert array result to dict
        """
        if type(iface) is list:
            if len(iface) == 1:
                return iface[0]
            else:
                _ifaces = {}
                for _iface in iface:
                    _ifaces[_iface['name']] = _iface
                return _ifaces
        elif type(iface) is dict:
            return iface
        return {}

    def __get_timestamp(self):
        """
        get timestamp of data collection
        """
        return self.__timestamp

    def __get_ifaces_info(self, path):
        """
        private methode
        the main function that scan /sys/class/net to collect interfaces informations
        """
        objArray = []
        # check if the path is directory and you have read access """
        if not os.path.isdir(path) or not os.access(path, os.R_OK):
            raise Exception('Error: you are not allowed')
        # let get the elements in this first level directory """
        try:
            netInterfaces = os.listdir(path)
        except Exception as Err:
            raise Exception('Error: Cannot read the main directory - ', Err)
        # let collect network interfaces """
        for iface in netInterfaces:
            netIface = {}
            if os.path.isdir(os.path.join(path, iface)):
                # create the interface object and begin the data collection """
                netIface['name'] = iface
                netIface['ip'] = self.ip_address(iface)
                netIface['mask'] = self.network_mask(iface)
                netIface['timestamp'] = self.__get_timestamp()
                if netIface['ip'] != '' and netIface['mask'] != '':
                    netIface['network_address'] = self.network_address(netIface['ip'], netIface['mask'])
                else:
                    netIface['network_address'] = ''
                netIfaceDir = os.path.join(path, iface)
                # get the interface params """
                try:
                    netIfaceParams = os.listdir(netIfaceDir)
                except IOError:
                    pass
                for param in netIfaceParams:
                    if os.path.isfile(os.path.join(netIfaceDir, param)):
                        # here we read every param file and we put the data collected on the  """
                        try:
                            # python 2 & 3 compatibility
                            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
                            if sys.version_info.major == 3:
                                fd = open(os.path.join(netIfaceDir, param), 'r', encoding='latin1')
                            else:
                                fd = open(os.path.join(netIfaceDir, param), 'r')
                            paramValue = fd.read()
                            try:
                                fd.close()
                            except Exception:
                                pass
                        except IOError:
                            paramValue = ''
                        if param == 'uevent':
                            netIface[param] = self.__uevent_as_list(paramValue.rstrip())
                        else:
                            netIface[param] = self.__convert_value(paramValue.rstrip())
                    if os.path.isdir(os.path.join(netIfaceDir, param)):
                        netIface[param] = self.__scan_object(os.path.join(netIfaceDir, param), param)
                objArray.append(netIface)
        return objArray

    def __scan_object(self, path, object_name):
        """
        private methode
        function used to scan the first level of sub directories in /sys/class/net/<iface>/
        """
        scan_obj = {}
        try:
            sub_objects = os.listdir(path)
        except IOError:
            pass
        for sub_object in sub_objects:
            if os.path.isfile(os.path.join(path, sub_object)):
                try:
                    # python 2 & 3 compatibility
                    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
                    if sys.version_info.major == 3:
                        __fd = open(os.path.join(path, sub_object), 'r', encoding='latin1')
                    else:
                        __fd = open(os.path.join(path, sub_object), 'r')
                    paramValue = __fd.readlines()
                    __fd.close()
                except IOError:
                    paramValue = ''
                ### paramValue = self.read_file_as_table(os.path.join(path, sub_object))
                if len(paramValue) == 1:
                    scan_obj[sub_object] = self.__convert_value(paramValue[0].rstrip())
                else:
                    if sub_object == 'uevent':
                        scan_obj[sub_object] = self.__uevent_as_list('\n'.join(paramValue))
                    else:
                        scan_obj[sub_object] = []
                        for val in paramValue:
                            scan_obj[sub_object].append(self.__convert_value(val.rstrip()))
            #if os.path.isdir(os.path.join(path, sub_object)):
                #scan_obj[sub_object] = __scan_object(os.path.join(path, sub_object), sub_object)
                #print 'Dir: ' + path + '/' + sub_object, sub_object
        return scan_obj

    def __convert_value(self, valuetoconvert):
        """
        private methode that convert from string to int or float or keep string if tye is not detected
        """
        _value = ''
        try:
            _value = int(valuetoconvert)
        except ValueError:
            try:
                _value = float(valuetoconvert)
            except ValueError:
                _value = valuetoconvert
        return _value

    def __get_routes(self, routefile):
        # Iface	Destination	Gateway 	Flags	RefCnt	Use	Metric	Mask		MTU	Window	IRTT
        _routing = []
        try:
            """
            python 2 & 3 compatibility
            UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 2: invalid continuation byte
            """
            if sys.version_info.major == 3:
                fd = open(routefile, 'r', encoding='latin1')
            else:
                fd = open(routefile, 'r')
            paramValue = fd.readlines()
        except IOError:
            paramValue = ''
            fd.close()
        if len(paramValue) == 1:
            return {}
        paramValue.pop(0)
        for route in paramValue:
            _route = route.split()
            _routing.append({
                'iface': _route[0],
                'x_dest': _route[1],
                'dest': self.reverse_ip(self.hex2ip(_route[1])),
                'x_gateway': _route[2],
                'gateway': self.reverse_ip(self.hex2ip(_route[2])),
                'flags': _route[3],
                'refcnt': _route[4],
                'use': _route[5],
                'metric': _route[6],
                'x_mask': _route[7],
                'mask': self.reverse_ip(self.hex2ip(_route[7])),
                'mtu': _route[8],
                'window': _route[9],
                'irtt': _route[10],
                'timestamp': self.__get_timestamp()
            })
        return _routing

    def __uevent_as_list(self, uevententry):
        __iface = {}
        __devtype = False
        for iface_type in uevententry.split('\n'):
            _iface_type = iface_type.split('=')
            if len(_iface_type) == 2:
                __iface[_iface_type[0].lower()] = _iface_type[1]
                if _iface_type[0].lower() == 'devtype':
                     __devtype = True
        if __devtype == False:
            __iface['devtype'] = 'unknown'
        return __iface


    ####################
    # Public Methodes
    ####################

    #######################
    # the as dict method
    #######################
    def as_dict(self):
        """
        return interfaces informations as dict result
        """
        return self.__ifaces_infos__

    def get_timestamp(self):
        """
        get timestamp of data collection
        """
        return self.timestamp

    def ifaces_as_dict(self):
        """
        return interfaces informations as dict result give the same result as self.as_dict()
        """
        return self.as_dict()
    
    def ifaces_statistics_as_dict(self):
        """
        return ifaces statistics as dict
        """
        __iface_statistics = {}
        for iface in self.as_dict():
            __iface_statistics[iface] = self.as_dict()[iface]['statistics']
            __iface_statistics[iface]['timetamp'] = self.get_timestamp()
        return __iface_statistics

    def iface_as_dict(self, ifacename):
        """
        return interfaces informations as dict result
        """
        if ifacename in self.as_dict():
            return self.as_dict()[ifacename]

    def list_interfaces(self):
        """
        list all interafces as list()
        """
        return [iface for iface in self.as_dict()]

    ####################
    # initial method
    ####################

    def refresh(self):
        """
        this function refresh the informations collected when the class is loaded
        if you want to work with fresh data use this function to reload the data updated
        """
        self.__init__()
    
    def reload(self):
        """
        same as self.refresh()
        """
        self.refresh()

    def ifaces_count(self):
        """
        return a number of detected interfaces
        """
        return len(self.ifaces_info())

    def ifaces_list(self):
        """
        get a list of interface name
        return array of string
        """
        iface_lst = []
        for iface in self.ifaces_info():
            iface_lst.append(iface['name'])
        return iface_lst

    def iface_info(self, ifaceName):
        """
        get specific interface name with full information
        return dict
        """
        for iface in self.ifaces_info():
            if iface['name'] == ifaceName:
                return iface
        return {}

    def ifaces_info(self):
        """
        get all interfaces informations (full collected information)
        """
        return self.__ifaces_info

    def ifaces_ifindex(self):
        """
        get all interfaces name and ifindex
        return array of dict
        """
        ifacesIndex = []
        for iface in self.ifaces_info():
            _iface = {
                'name': iface['name'],
                'iflink': iface['iflink'],
                'ifindex': iface['ifindex']
            }
            ifacesIndex.append(_iface)
        return ifacesIndex

    def ifaces_iflink(self):
        """
        get all interfaces name and iflink
        return array of dict
        """
        ifacesLink = []
        for iface in self.ifaces_info():
            _iface = {
                'name': iface['name'],
                'iflink': iface['iflink'],
                'ifindex': iface['ifindex']
            }
            ifacesLink.append(_iface)
        return ifacesLink

    def ifaces_ifindex_iflink(self):
        """
        get all interfaces with brief informations (name, ifindex, iflink, ip and mask)
        return an array of dict
        """
        ifaceIndexLink = []
        for iface in self.ifaces_info():
            _iface = {
                'name': iface['name'],
                'ifindex': iface['ifindex'],
                'iflink': iface['iflink'],
                'ip': iface['ip'],
                'mask': iface['mask'],
                'network_address': iface['network_address'],
                'operstate': iface['operstate'],
                'timestamp': self.__get_timestamp()
            }
            ifaceIndexLink.append(_iface)
        return ifaceIndexLink

    def iface_by_uid(self, identifier, value, info='full'):
        """
        get interfaces by defined identifier and value, the third parametre info allow 
        the choise to return the result as a full data or briefly
        
        the identifier can be any key value of the class definition
        this funtion is used by self.getifaceByIndex() and self.getifaceByLink()

        return dict
        """
        _value = str(value)
        for iface in self.ifaces_info():
            try:
                if iface[identifier] == _value:
                    if info == 'brief':
                        return {
                            'name': iface['name'],
                            'ifindex': iface['ifindex'],
                            'iflink': iface['iflink'],
                            'ip': iface['ip'],
                            'mask': iface['mask'],
                            'network_address': iface['network_address'],
                            'operstate': iface['operstate'],
                            'timestamp': self.__get_timestamp()
                        }
                    elif info == 'full':
                        return iface
            except Exception:
                pass
        return {}
    
    def iface_by_ifindex(self, ifindex, info='full'):
        """
        get interface that have ifindex=X
        ifindex is located in /sys/class/net/<iface>/ifindex
        return dict
        """
        return self.iface_by_uid('ifindex', ifindex, info)

    def iface_by_iflink(self, iflink, info='full'):
        """
        get interface that have iflink=X
        ifindex is located in /sys/class/net/<iface>/iflink
        return dict
        """
        return self.iface_by_uid('iflink', iflink, info)

    def ifaces_by_status(self, status, info='full'):
        """
        get interface by status, this function is used by self.getifacesUp() and self.getifacesDown()
        return an array with dict
        """
        _ifaces = []
        for iface in self.ifaces_info():
            try:
                if iface['operstate'] == status:
                    if info == 'brief':
                        _iface = {
                            'name': iface['name'],
                            'ifindex': iface['ifindex'],
                            'iflink': iface['iflink'],
                            'ip': iface['ip'],
                            'mask': iface['mask'],
                            'network_address': iface['network_address'],
                            'operstate': iface['operstate'],
                            'timestamp': self.__get_timestamp()
                        }
                    elif info == 'full':
                        _iface = iface
                    _ifaces.append(_iface)
            except Exception:
                pass
        return _ifaces

    def ifaces_up(self, info='full'):
        """
        get interface up only
        return an array with dict
        """
        return self.ifaces_by_status('up', info)

    def ifaces_down(self, info='full'):
        """
        get interface down and other status
        return an array with dict
        """
        return self.ifaces_by_status('down', info)

    #def get_ip_address(ifname):
    #    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

    def ifaces_type(self):
        """
        return a list of all interfaces with uevent that give device type
        """
        #'uevent': 'DEVTYPE=wlan\nINTERFACE=wlp2s0\nIFINDEX=3'
        _ifacetype = []
        for iface in self.ifaces_info():
            _iface = {
                'name': iface['name'],
                'ip': iface['ip'],
                'mask': iface['mask'],
                'network_address': iface['network_address'],
                'operstate': iface['operstate'],
                'timestamp': self.__get_timestamp(),
                'uevent': iface['uevent']
            }
            _ifacetype.append(_iface)
        return _ifacetype

    def iface_type(self, ifacename):
        """
        return a dict of specific interface with interface_type if the interface is not found return empty dict
        """
        #'uevent': 'DEVTYPE=wlan\nINTERFACE=wlp2s0\nIFINDEX=3'
        for iface in self.ifaces_type():
            if iface['name'] == ifacename:
                return iface
        return {}

    def ifaces_network_config(self):
        """
        get the interfaces network configuration only
        """
        _netconf = []
        for iface in self.ifaces_info():
            _netconf.append({
                'name': iface['name'], 
                'ip': iface['ip'],
                'mask': iface['mask'],
                'network_address': iface['network_address'],
                'mtu': iface['mtu'],
                'link_mode': iface['link_mode'],
                'proto_down': iface['proto_down'],
                'operstate': iface['operstate'],
                'broadcast': iface['broadcast'],
                'speed': iface['speed'],
                'addr_assign_type': iface['addr_assign_type'],
                'type': iface['type'],
                'name_assign_type': iface['name_assign_type'],
                'dev_id': iface['dev_id'],
                'address': iface['address'],
                'timestamp': self.__get_timestamp()
            })
        return _netconf
    
    def iface_network_config(self, ifacename):
        """
        get specific interface network configuration only, return dict
        """
        for iface in self.ifaces_info():
            if iface['name'] == ifacename:
                return {
                    'name': iface['name'], 
                    'ip': iface['ip'],
                    'mask': iface['mask'],
                    'network_address': iface['network_address'],
                    'mtu': iface['mtu'],
                    'link_mode': iface['link_mode'],
                    'proto_down': iface['proto_down'],
                    'operstate': iface['operstate'],
                    'broadcast': iface['broadcast'],
                    'speed': iface['speed'],
                    'addr_assign_type': iface['addr_assign_type'],
                    'type': iface['type'],
                    'name_assign_type': iface['name_assign_type'],
                    'dev_id': iface['dev_id'],
                    'address': iface['address'],
                    'timestamp': self.__get_timestamp()
                }
            else:
                return {}

    def ifaces_statistics(self):
        """
        return a list of all interfaces with statistics
        """
        _ifacestatistics = []
        for iface in self.ifaces_info():
            _ifacestatistics.append({
                'name': iface['name'], 
                'ip': iface['ip'],
                'mask': iface['mask'],
                'network_address': iface['network_address'],
                'mtu': iface['mtu'],
                'ifindex': iface['ifindex'],
                'iflink': iface['iflink'],
                'statistics': iface['statistics'],
                'timestamp': self.__get_timestamp()
            })
        return _ifacestatistics
    
    def iface_statistics(self, ifacename):
        """
        return a dict of specific interface with statistics
        """
        for iface in self.ifaces_statistics():
            if iface['name'] == ifacename:
                return iface
        return {}

    def ifaces_routes(self):
        """
        return the routing table as array.
        """
        return self.__ifaces_routes

    def iface_routes(self, ifacename):
        """
        return the routing table of specific interface.
        """
        _iface_routes = []
        for iface_route in self.ifaces_routes():
            if iface_route['iface'] == 'ifacename':
                _iface_routes.append(iface_route)
        return _iface_routes


