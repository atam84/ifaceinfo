# Package udpconn Documentation

## Class Conn
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
### \_\_init\_\_
```py

def __init__(self, procfilename, protocole)

```



initialization method that inherit IfaceInfoTools class


### conn
```py

def conn(self)

```



(alias) same is connexion(self)


### conn\_by\_status
```py

def conn_by_status(self, connstatus)

```



get {tcp, udp} connexion with last_ack '09' {tcp, udp} status


### connexion
```py

def connexion(self)

```



return a list of all {tcp, udp} connexion


### get\_close\_conn
```py

def get_close_conn(self)

```



get {tcp, udp} connexion with close '07' {tcp, udp} status


### get\_close\_wait\_conn
```py

def get_close_wait_conn(self)

```



### get\_closing\_conn
```py

def get_closing_conn(self)

```



get {tcp, udp} connexion with closing '0B' {tcp, udp} status


### get\_established\_conn
```py

def get_established_conn(self)

```



get {tcp, udp} connexion with established '01' {tcp, udp} status


### get\_fin\_wait1\_conn
```py

def get_fin_wait1_conn(self)

```



get {tcp, udp} connexion with fin_wait1 '04' {tcp, udp} status


### get\_fin\_wait2\_conn
```py

def get_fin_wait2_conn(self)

```



get {tcp, udp} connexion with fin_wait2 '05' {tcp, udp} status


### get\_last\_ack\_conn
```py

def get_last_ack_conn(self)

```



get {tcp, udp} connexion with last_ack '09' {tcp, udp} status


### get\_listen\_conn
```py

def get_listen_conn(self)

```



get {tcp, udp} connexion with listen '0A' {tcp, udp} status


### get\_max\_state\_conn
```py

def get_max_state_conn(self)

```



get {tcp, udp} connexion with max_state '0C' {tcp, udp} status


### get\_syn\_recv\_conn
```py

def get_syn_recv_conn(self)

```



get {tcp, udp} connexion with recv '03' {tcp, udp} status


### get\_syn\_sent\_conn
```py

def get_syn_sent_conn(self)

```



get {tcp, udp} connexion with syn_sent '02' {tcp, udp} status


### get\_time\_wait\_conn
```py

def get_time_wait_conn(self)

```



get {tcp, udp} connexion with time_wait '06' {tcp, udp} status


### hex2ip
```py

def hex2ip(self, x_addr)

```



private methode
convert hexadecimal representation to string decimal ip address
return string (as ip address representation)


### ip2hex
```py

def ip2hex(self, addr)

```



private methode
convert string decimal ip address to hexadecimal representation
return string (as hex representation)


### ip\_address
```py

def ip_address(self, ifacename)

```



private methode
get ip address of interface using socket interface


### local\_addrs
```py

def local_addrs(self)

```



get dict of local address and ports list
{
    'local_host_ip': [list of ports]
}


### local\_ports
```py

def local_ports(self)

```



get list of ports used by local host [listen, established, ...]


### network\_address
```py

def network_address(self, ipaddr, mask)

```



private methode
used to calculate the network address


### network\_mask
```py

def network_mask(self, ifacename)

```



private methode
get net mask address of interface using socket interface


### read\_file\_as\_table
```py

def read_file_as_table(self, filename)

```



private method that read given file completly and return it as list of lines


### remote\_addrs
```py

def remote_addrs(self)

```



get dict of remote address and ports list
{
    'remote_host_ip': [list of ports],
}


### remote\_ports
```py

def remote_ports(self)

```



get list of ports used by remote host


### reverse\_ip
```py

def reverse_ip(self, ipaddress)

```



Private method that reverse ip address




## Class UDPConn
None
### \_\_init\_\_
```py

def __init__(self)

```



### conn
```py

def conn(self)

```



(alias) same is connexion(self)


### conn\_by\_status
```py

def conn_by_status(self, connstatus)

```



get {tcp, udp} connexion with last_ack '09' {tcp, udp} status


### connexion
```py

def connexion(self)

```



return a list of all {tcp, udp} connexion


### get\_close\_conn
```py

def get_close_conn(self)

```



get {tcp, udp} connexion with close '07' {tcp, udp} status


### get\_close\_wait\_conn
```py

def get_close_wait_conn(self)

```



### get\_closing\_conn
```py

def get_closing_conn(self)

```



get {tcp, udp} connexion with closing '0B' {tcp, udp} status


### get\_established\_conn
```py

def get_established_conn(self)

```



get {tcp, udp} connexion with established '01' {tcp, udp} status


### get\_fin\_wait1\_conn
```py

def get_fin_wait1_conn(self)

```



get {tcp, udp} connexion with fin_wait1 '04' {tcp, udp} status


### get\_fin\_wait2\_conn
```py

def get_fin_wait2_conn(self)

```



get {tcp, udp} connexion with fin_wait2 '05' {tcp, udp} status


### get\_last\_ack\_conn
```py

def get_last_ack_conn(self)

```



get {tcp, udp} connexion with last_ack '09' {tcp, udp} status


### get\_listen\_conn
```py

def get_listen_conn(self)

```



get {tcp, udp} connexion with listen '0A' {tcp, udp} status


### get\_max\_state\_conn
```py

def get_max_state_conn(self)

```



get {tcp, udp} connexion with max_state '0C' {tcp, udp} status


### get\_syn\_recv\_conn
```py

def get_syn_recv_conn(self)

```



get {tcp, udp} connexion with recv '03' {tcp, udp} status


### get\_syn\_sent\_conn
```py

def get_syn_sent_conn(self)

```



get {tcp, udp} connexion with syn_sent '02' {tcp, udp} status


### get\_time\_wait\_conn
```py

def get_time_wait_conn(self)

```



get {tcp, udp} connexion with time_wait '06' {tcp, udp} status


### hex2ip
```py

def hex2ip(self, x_addr)

```



private methode
convert hexadecimal representation to string decimal ip address
return string (as ip address representation)


### ip2hex
```py

def ip2hex(self, addr)

```



private methode
convert string decimal ip address to hexadecimal representation
return string (as hex representation)


### ip\_address
```py

def ip_address(self, ifacename)

```



private methode
get ip address of interface using socket interface


### local\_addrs
```py

def local_addrs(self)

```



get dict of local address and ports list
{
    'local_host_ip': [list of ports]
}


### local\_ports
```py

def local_ports(self)

```



get list of ports used by local host [listen, established, ...]


### network\_address
```py

def network_address(self, ipaddr, mask)

```



private methode
used to calculate the network address


### network\_mask
```py

def network_mask(self, ifacename)

```



private methode
get net mask address of interface using socket interface


### read\_file\_as\_table
```py

def read_file_as_table(self, filename)

```



private method that read given file completly and return it as list of lines


### refresh
```py

def refresh(self)

```



this function refresh the informations collected when the class is loaded
if you want to work with fresh data use this function to reload the data updated


### reload
```py

def reload(self)

```



same as self.refresh()


### remote\_addrs
```py

def remote_addrs(self)

```



get dict of remote address and ports list
{
    'remote_host_ip': [list of ports],
}


### remote\_ports
```py

def remote_ports(self)

```



get list of ports used by remote host


### reverse\_ip
```py

def reverse_ip(self, ipaddress)

```



Private method that reverse ip address




