"""
@ Date: 2024-04-30 08:41:51
@ LastEditors: sky
@ LastEditTime: 2024-05-08 10:10:21
@ FilePath: /SkyTunnel/app/public/stundev.py
@ Desc: 
"""

# Full Cone NAT（全锥型NAT）：在Full Cone NAT中，内部私有IP地址和端口与外部公共IP地址和端口一一映射，这意味着一旦建立连接，所有来自外部IP地址的数据包都可以通过相同的映射进行传输。

# Restric NAT（限制锥型NAT）：在Restricted Cone NAT中，只有在内部主机首先向外部主机发送数据包后，外部主机才能通过相同的映射向内部主机发送数据包。这个映射是基于目标IP地址和端口的。

# Port Restricted Cone NAT（端口限制锥型NAT）：类似于Restricted Cone NAT，但外部主机必须通过相同的映射源端口发送数据包。

# Symmetric NAT（对称型NAT）：如前面所述，Symmetric NAT会根据通信的目的地址和端口为内部主机分配不同的公共IP地址和端口。

# Carrier-grade NAT（CGNAT）：CGNAT是一种大规模NAT，用于将多个内部私有IP地址转换为较少的公共IP地址。它通常由互联网服务提供商在面临IPv4地址短缺时使用。

import stun

def get_public_ip_and_port(local_ip, local_port):
    response = stun.get_ip_info(source_ip=local_ip, source_port=local_port)
    stun_type = response[0]
    public_ip = response[1]
    public_port = response[2]
    return stun_type, public_ip, public_port

local_ip = '10.23.222.196'
local_port = 5000
stun_type,public_ip, public_port = get_public_ip_and_port(local_ip, local_port)
print(stun_type)

print("Public IP:", public_ip)
print("Public Port:", public_port)
