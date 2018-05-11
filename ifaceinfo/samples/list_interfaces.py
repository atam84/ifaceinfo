#!/usr/bin/env python

#
# Author : Mohamed Amine TAMDY
# Email  : amine.tamdy@gmail.com
# Github : https://github.com/atam84/ifaceinfo
#


import sys
sys.path.append('../')
from ifaceinfo import InterfacesInfos
from pprint import pprint

class COLOR:
    class fg:
        BLACK   = '\033[30m'
        RED     = '\033[31m'
        GREEN   = '\033[32m'
        YELLOW  = '\033[33m'
        BLUE    = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN    = '\033[36m'
        WHITE   = '\033[37m'
        RESET   = '\033[39m'

    class bg:
        BLACK   = '\033[40m'
        RED     = '\033[41m'
        GREEN   = '\033[42m'
        YELLOW  = '\033[43m'
        BLUE    = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN    = '\033[46m'
        WHITE   = '\033[47m'
        RESET   = '\033[49m'

    class style:
        BOLD    = '\033[1m'
        DIM       = '\033[2m'
        NORMAL    = '\033[22m'
        RESET_ALL = '\033[0m'
        UNDERLINE = '\033[4m'

cl = COLOR

def get_network_interfaces():
    ifaces = InterfacesInfos().ifaces_as_dict()
    _report = {
        'n_iface': 0,
        'iface_oper_up': 0,
        'iface_oper_down': 0,
        'iface_oper_unknown': 0,
        'br_count': 0,
    }
    for interface in ifaces:
        _ifacename =  cl.style.BOLD + interface + cl.style.RESET_ALL
        _report['n_iface'] += 1
        _operstate = ifaces[interface]['operstate']
        if _operstate == 'up':
            _report['iface_oper_up'] += 1
            _operstate = cl.fg.GREEN + _operstate + cl.fg.RESET
        elif _operstate == 'down':
            _report['iface_oper_down'] += 1
            _operstate = cl.fg.RED + _operstate + cl.fg.RESET
        else:
            _report['iface_oper_unknown'] += 1
            _operstate = cl.fg.YELLOW + _operstate + cl.fg.RESET
        
        _collisions = ifaces[interface]['statistics']['collisions']
        if _collisions == 0:
            _collisions = cl.fg.GREEN + str(_collisions) + cl.fg.RESET
        else:
            _collisions = cl.fg.RED + str(_collisions) + cl.fg.RESET
        _multicast = str(ifaces[interface]['statistics']['multicast'])
        _tx_errors = ifaces[interface]['statistics']['tx_errors']
        if _tx_errors == 0:
            _tx_errors = cl.fg.GREEN + str(_tx_errors) + cl.fg.RESET
        elif _tx_errors <= 100:
            _tx_errors = cl.fg.YELLOW + str(_tx_errors) + cl.fg.RESET
        else:
            _tx_errors = cl.fg.RED + str(_tx_errors) + cl.fg.RESET
        _rx_errors = ifaces[interface]['statistics']['rx_errors']
        if _rx_errors == 0:
            _rx_errors = cl.fg.GREEN + str(_rx_errors) + cl.fg.RESET
        elif _rx_errors <= 100:
            _rx_errors = cl.fg.YELLOW + str(_rx_errors) + cl.fg.RESET
        else:
            _rx_errors = cl.fg.RED + str(_rx_errors) + cl.fg.RESET
        _devtype = ifaces[interface]['uevent']['devtype']
        if _devtype == 'bridge':
            _report['br_count'] += 1
            _devtype = cl.style.BOLD + _devtype + cl.style.RESET_ALL
        elif _devtype == 'wlan':
            _devtype = cl.style.BOLD + cl.fg.MAGENTA + _devtype + cl.style.RESET_ALL
        elif _devtype == 'unknown':
            _devtype = cl.style.BOLD + cl.fg.BLUE + _devtype + cl.style.RESET_ALL
        else:
            _devtype = cl.style.BOLD + cl.fg.YELLOW + _devtype + cl.style.RESET_ALL
        _marker = cl.fg.YELLOW + '**' + cl.fg.RESET
        print('{} interface name: {}    id: {}     type: {}'.format(_marker, _ifacename, ifaces[interface]['dev_id'], ifaces[interface]['type']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('dev type', _devtype, 'operstate', _operstate))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('address', ifaces[interface]['address'], 'iface alias', ifaces[interface]['ifalias']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('iface link', str(ifaces[interface]['iflink']), 'iface index', str(ifaces[interface]['ifindex'])))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('ip', ifaces[interface]['ip'], 'mask', ifaces[interface]['mask']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('network', ifaces[interface]['network_address'],'mtu', str(ifaces[interface]['mtu'])))
        #ifaces[interface]['timestamp']
        #ifaces[interface]['name_assign_type']
        print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'interface statistics:' + cl.style.RESET_ALL))
        print('        {:20s} {:10s} {:14s}  {:10s}'.format('multicast       :', _multicast, 'collisions      :', _collisions))
        print('        {:20s} {}/{}'.format('bytes (tx/rx)   :', str(ifaces[interface]['statistics']['tx_bytes']), str(ifaces[interface]['statistics']['rx_bytes'])))
        print('        {:20s} {}/{}'.format('packets (tx/rx) :', str(ifaces[interface]['statistics']['tx_packets']), str(ifaces[interface]['statistics']['rx_packets'])))
        print('        {:20s} {}/{}'.format('errors (tx/rx)  :', _tx_errors, _rx_errors))
        if ifaces[interface]['uevent']['devtype'] == 'bridge':
            if 'lower' in ifaces[interface]:
                print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'bridge connected interfaces:' + cl.style.RESET_ALL))
                for key in ifaces[interface]['lower']:
                    #if key.startswith('lower_'):
                    print('        {:20s} {:20s} {:s}'.format(ifaces[interface]['lower'][key]['uevent']['interface'], ifaces[interface]['lower'][key]['address'], ifaces[interface]['lower'][key]['operstate']))
        else:
            if 'upper' in ifaces[interface]:
                print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'device connected on bridge:' + cl.style.RESET_ALL))
                for key in ifaces[interface]['upper']:
                    #if key.startswith('upper_'):
                    print('        {:20s} {:20s} {:s}'.format(ifaces[interface]['upper'][key]['uevent']['interface'], ifaces[interface]['upper'][key]['address'], ifaces[interface]['upper'][key]['operstate']))
        print('\n')
    print('---------------')
    #print('{}{} network interfaces that include {} bridge listed where {} up, {} down and {} with unknown status.{}'.format(cl.fg.WHITE, _report['n_iface'], _report['br_count'], _report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown'], cl.fg.RESET))
    print('{}{}'.format(cl.style.BOLD, cl.fg.WHITE))
    print('{} network interfaces that include {} bridge listed'.format(_report['n_iface'],_report['br_count']))
    print('{} up, {} down and {} with unknown status.'.format(_report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown']))
    print('{}'.format(cl.style.RESET_ALL))
    print('---------------')


if __name__ == '__main__':
    get_network_interfaces()

