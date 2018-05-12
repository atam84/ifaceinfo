import os
import sys
import socket
import fcntl
import struct
import time
from pprint import pprint



def ipv6_struct(ifacename):
    from pprint import pprint
    _fdsock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    _structpack = struct.pack('256s', ifacename.encode())
    print(ifacename)
    print('Socket :')
    pprint(_fdsock)
    print('Struct packed :')
    pprint(_structpack)
    print('system call ioctl :')
    _ioctl = fcntl.ioctl(_fdsock, 0x8915, _structpack)
    pprint(_ioctl)
    #pprint(_ioctl[20:24])
    #addr = socket.inet_ntop(socket.AF_INET, _ioctl[20:24])
    return 'addr'


if __name__ == '__main__':
    #pprint(ipv6_struct('vethe69ab97'))
    pprint(ipv6_struct('wlp2s0'))

'''
Very important
https://stackoverflow.com/questions/41940483/parse-ipv6-addresses-from-proc-net-tcp6-python-2-7
https://gist.github.com/kamalmarhubi/1dfc1fa302916e21975d

IPv6:

struct sockaddr_in6 {
    sa_family_t     sin6_family;   /* AF_INET6 */
    in_port_t       sin6_port;     /* port number */
    uint32_t        sin6_flowinfo; /* IPv6 flow information */
    struct in6_addr sin6_addr;     /* IPv6 address */
    uint32_t        sin6_scope_id; /* Scope ID (new in 2.4) */
};

struct in6_addr {
    unsigned char   s6_addr[16];   /* IPv6 address */   //// B 	unsigned char
};

'''

'''
IPv4:
#include <netinet/in.h>

struct sockaddr_in {
    short            sin_family;   // e.g. AF_INET
    unsigned short   sin_port;     // e.g. htons(3490)
    struct in_addr   sin_addr;     // see struct in_addr, below
    char             sin_zero[8];  // zero this if you want to
};

struct in_addr {
    unsigned long s_addr;  // load with inet_aton()  ////   L 	unsigned long 	integer
};

Examples:
struct sockaddr_in myaddr;
int s;

myaddr.sin_family = AF_INET;
myaddr.sin_port = htons(3490);
inet_aton("63.161.169.137", &myaddr.sin_addr.s_addr);

s = socket(PF_INET, SOCK_STREAM, 0);
bind(s, (struct sockaddr*)myaddr, sizeof(myaddr));
'''

'''
['AF_APPLETALK', 'AF_ASH', 'AF_ATMPVC', 'AF_ATMSVC', 'AF_AX25', 'AF_BLUETOOTH', 'AF_BRIDGE', 'AF_DECnet', 'AF_ECONET', 
'AF_INET', 'AF_INET6', 'AF_IPX', 'AF_IRDA', 'AF_KEY', 'AF_LLC', 'AF_NETBEUI', 'AF_NETLINK', 'AF_NETROM', 'AF_PACKET', 
'AF_PPPOX', 'AF_ROSE', 'AF_ROUTE', 'AF_SECURITY', 'AF_SNA', 'AF_TIPC', 'AF_UNIX', 'AF_UNSPEC', 'AF_WANPIPE', 'AF_X25', 
'AI_ADDRCONFIG', 'AI_ALL', 'AI_CANONNAME', 'AI_NUMERICHOST', 'AI_NUMERICSERV', 'AI_PASSIVE', 'AI_V4MAPPED', 'BDADDR_ANY', 
'BDADDR_LOCAL', 'BTPROTO_HCI', 'BTPROTO_L2CAP', 'BTPROTO_RFCOMM', 'BTPROTO_SCO', 'CAPI', 'EAI_ADDRFAMILY', 'EAI_AGAIN', 
'EAI_BADFLAGS', 'EAI_FAIL', 'EAI_FAMILY', 'EAI_MEMORY', 'EAI_NODATA', 'EAI_NONAME', 'EAI_OVERFLOW', 'EAI_SERVICE', 
'EAI_SOCKTYPE', 'EAI_SYSTEM', 'EBADF', 'EINTR', 'HCI_DATA_DIR', 'HCI_FILTER', 'HCI_TIME_STAMP', 'INADDR_ALLHOSTS_GROUP', 
'INADDR_ANY', 'INADDR_BROADCAST', 'INADDR_LOOPBACK', 'INADDR_MAX_LOCAL_GROUP', 'INADDR_NONE', 'INADDR_UNSPEC_GROUP', 
'IPPORT_RESERVED', 'IPPORT_USERRESERVED', 'IPPROTO_AH', 'IPPROTO_DSTOPTS', 'IPPROTO_EGP', 'IPPROTO_ESP', 'IPPROTO_FRAGMENT', 
'IPPROTO_GRE', 'IPPROTO_HOPOPTS', 'IPPROTO_ICMP', 'IPPROTO_ICMPV6', 'IPPROTO_IDP', 'IPPROTO_IGMP', 'IPPROTO_IP', 
'IPPROTO_IPIP', 'IPPROTO_IPV6', 'IPPROTO_NONE', 'IPPROTO_PIM', 'IPPROTO_PUP', 'IPPROTO_RAW', 'IPPROTO_ROUTING', 
'IPPROTO_RSVP', 'IPPROTO_TCP', 'IPPROTO_TP', 'IPPROTO_UDP', 'IPV6_CHECKSUM', 'IPV6_DONTFRAG', 'IPV6_DSTOPTS', 
'IPV6_HOPLIMIT', 'IPV6_HOPOPTS', 'IPV6_JOIN_GROUP', 'IPV6_LEAVE_GROUP', 'IPV6_MULTICAST_HOPS', 'IPV6_MULTICAST_IF', 
'IPV6_MULTICAST_LOOP', 'IPV6_NEXTHOP', 'IPV6_PATHMTU', 'IPV6_PKTINFO', 'IPV6_RECVDSTOPTS', 'IPV6_RECVHOPLIMIT', 
'IPV6_RECVHOPOPTS', 'IPV6_RECVPATHMTU', 'IPV6_RECVPKTINFO', 'IPV6_RECVRTHDR', 'IPV6_RECVTCLASS', 'IPV6_RTHDR', 
'IPV6_RTHDRDSTOPTS', 'IPV6_RTHDR_TYPE_0', 'IPV6_TCLASS', 'IPV6_UNICAST_HOPS', 'IPV6_V6ONLY', 'IP_ADD_MEMBERSHIP', 
'IP_DEFAULT_MULTICAST_LOOP', 'IP_DEFAULT_MULTICAST_TTL', 'IP_DROP_MEMBERSHIP', 'IP_HDRINCL', 'IP_MAX_MEMBERSHIPS', 
'IP_MULTICAST_IF', 'IP_MULTICAST_LOOP', 'IP_MULTICAST_TTL', 'IP_OPTIONS', 'IP_RECVOPTS', 'IP_RECVRETOPTS', 'IP_RETOPTS', 
'IP_TOS', 'IP_TTL', 'MSG_CTRUNC', 'MSG_DONTROUTE', 'MSG_DONTWAIT', 'MSG_EOR', 'MSG_OOB', 'MSG_PEEK', 'MSG_TRUNC', 
'MSG_WAITALL', 'MethodType', 'NETLINK_DNRTMSG', 'NETLINK_FIREWALL', 'NETLINK_IP6_FW', 'NETLINK_NFLOG', 'NETLINK_ROUTE', 
'NETLINK_USERSOCK', 'NETLINK_XFRM', 'NI_DGRAM', 'NI_MAXHOST', 'NI_MAXSERV', 'NI_NAMEREQD', 'NI_NOFQDN', 'NI_NUMERICHOST', 
'NI_NUMERICSERV', 'PACKET_BROADCAST', 'PACKET_FASTROUTE', 'PACKET_HOST', 'PACKET_LOOPBACK', 'PACKET_MULTICAST', 
'PACKET_OTHERHOST', 'PACKET_OUTGOING', 'PF_PACKET', 'RAND_add', 'RAND_egd', 'RAND_status', 'SHUT_RD', 'SHUT_RDWR', 
'SHUT_WR', 'SOCK_DGRAM', 'SOCK_RAW', 'SOCK_RDM', 'SOCK_SEQPACKET', 'SOCK_STREAM', 'SOL_HCI', 'SOL_IP', 'SOL_SOCKET', 
'SOL_TCP', 'SOL_TIPC', 'SOL_UDP', 'SOMAXCONN', 'SO_ACCEPTCONN', 'SO_BROADCAST', 'SO_DEBUG', 'SO_DONTROUTE', 'SO_ERROR', 
'SO_KEEPALIVE', 'SO_LINGER', 'SO_OOBINLINE', 'SO_RCVBUF', 'SO_RCVLOWAT', 'SO_RCVTIMEO', 'SO_REUSEADDR', 'SO_REUSEPORT', 
'SO_SNDBUF', 'SO_SNDLOWAT', 'SO_SNDTIMEO', 'SO_TYPE', 'SSL_ERROR_EOF', 'SSL_ERROR_INVALID_ERROR_CODE', 'SSL_ERROR_SSL', 
'SSL_ERROR_SYSCALL', 'SSL_ERROR_WANT_CONNECT', 'SSL_ERROR_WANT_READ', 'SSL_ERROR_WANT_WRITE', 'SSL_ERROR_WANT_X509_LOOKUP', 
'SSL_ERROR_ZERO_RETURN', 'SocketType', 'StringIO', 'TCP_CORK', 'TCP_DEFER_ACCEPT', 'TCP_INFO', 'TCP_KEEPCNT', 
'TCP_KEEPIDLE', 'TCP_KEEPINTVL', 'TCP_LINGER2', 'TCP_MAXSEG', 'TCP_NODELAY', 'TCP_QUICKACK', 'TCP_SYNCNT', 
'TCP_WINDOW_CLAMP', 'TIPC_ADDR_ID', 'TIPC_ADDR_NAME', 'TIPC_ADDR_NAMESEQ', 'TIPC_CFG_SRV', 'TIPC_CLUSTER_SCOPE', 
'TIPC_CONN_TIMEOUT', 'TIPC_CRITICAL_IMPORTANCE', 'TIPC_DEST_DROPPABLE', 'TIPC_HIGH_IMPORTANCE', 'TIPC_IMPORTANCE', 
'TIPC_LOW_IMPORTANCE', 'TIPC_MEDIUM_IMPORTANCE', 'TIPC_NODE_SCOPE', 'TIPC_PUBLISHED', 'TIPC_SRC_DROPPABLE', 
'TIPC_SUBSCR_TIMEOUT', 'TIPC_SUB_CANCEL', 'TIPC_SUB_PORTS', 'TIPC_SUB_SERVICE', 'TIPC_TOP_SRV', 'TIPC_WAIT_FOREVER', 
'TIPC_WITHDRAWN', 'TIPC_ZONE_SCOPE', '_GLOBAL_DEFAULT_TIMEOUT', '__all__', '__builtins__', '__doc__', '__file__', 
'__name__', '__package__', '_closedsocket', '_delegate_methods', '_fileobject', '_m', '_realsocket', '_socket', 
'_socketmethods', '_socketobject', '_ssl', 'create_connection', 'errno', 'error', 'fromfd', 'gaierror', 'getaddrinfo', 
'getdefaulttimeout', 'getfqdn', 'gethostbyaddr', 'gethostbyname', 'gethostbyname_ex', 'gethostname', 'getnameinfo', 
'getprotobyname', 'getservbyname', 'getservbyport', 'has_ipv6', 'herror', 'htonl', 'htons', 'inet_aton', 'inet_ntoa', 
'inet_ntop', 'inet_pton', 'm', 'meth', 'ntohl', 'ntohs', 'os', 'p', 'partial', 'setdefaulttimeout', 'socket', 
'socketpair', 'ssl', 'sslerror', 'sys', 'timeout', 'warnings']
'''