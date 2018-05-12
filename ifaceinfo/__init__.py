import sys

if sys.version_info.major >= 3:
    from ifaceinfo.ifaceinfo import InterfacesInfos
    from ifaceinfo.ifaceroutes import InterfacesRoutes
    from ifaceinfo.ifaceinfotools import IfaceInfoTools, FileReader, Conn
    from ifaceinfo.tcpconn import TCPConn
    from ifaceinfo.udpconn import UDPConn
    from ifaceinfo.tcpconn import TCP6Conn
    from ifaceinfo.udpconn import UDP6Conn
    from ifaceinfo.ifaceversion import version
else:
    from ifaceinfo import InterfacesInfos
    from ifaceroutes import InterfacesRoutes
    from ifaceinfotools import IfaceInfoTools, FileReader, Conn
    from tcpconn import TCPConn
    from udpconn import UDPConn
    from tcpconn import TCP6Conn
    from udpconn import UDP6Conn
    from ifaceversion import version