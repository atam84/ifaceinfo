import os
from pprint import pprint

def sdir(path):
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
                    netIface[param] = scan_object(os.path.join(netIfaceDir, param), param)
            objArray.append(netIface)
    return objArray

def scan_object(path, object_name):
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

#def main():
#    ifaces = lxifaces()
#    pprint('iface names : ' + ifaces.list())

if __name__ == '__main__':
    pprint(sdir("/sys/class/net"))

