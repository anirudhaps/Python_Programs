# Copyright (C) 2014 SDN Hub
#
# Licensed under the GNU GENERAL PUBLIC LICENSE, Version 3.
# You may not use this file except in compliance with this License.
# You may obtain a copy of the License at
#
#    http://www.gnu.org/licenses/gpl-3.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.


from pox.core import core
from pox.lib.addresses import IPAddr,EthAddr,parse_cidr
from pox.lib.revent import EventContinue,EventHalt
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
import sys
import math

log = core.getLogger()

############## Global constants #############

virtual_ip = IPAddr("10.0.0.5")
virtual_mac = EthAddr("00:00:00:00:00:05")

server = {}
server[0] = {'ip':IPAddr("10.0.0.2"), 'mac':EthAddr("00:00:00:00:00:02"), 'outport': 2}
server[1] = {'ip':IPAddr("10.0.0.3"), 'mac':EthAddr("00:00:00:00:00:03"), 'outport': 3}
server[2] = {'ip':IPAddr("10.0.0.4"), 'mac':EthAddr("00:00:00:00:00:04"), 'outport': 4}
total_servers = len(server)

server_index = 0
count = 1

################ Handlers ###################

def _handle_PacketIn (event):
    global server_index
    global count
    packet = event.parsed

    # Only handle IPv4 flows
    if (not event.parsed.find("ipv4")):
        return EventContinue

    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)

    # Only handle traffic destined to virtual IP
    if (msg.match.nw_dst != virtual_ip):
        return EventContinue

    # selection of servers in (0.5,0.25,0.25) ratio
    s1c = math.ceil(total_servers/2.0)
    s2c = math.ceil(total_servers/4.0)
    s3c = math.ceil(total_servers/4.0)
    sumrec = s1c + s2c + s3c
    if count<=s1c:
        index = server_index % total_servers
        #print index
        count+=1
    else:
        server_index += 1
        index = server_index % total_servers
        #print index
        count+=1
        if count>sumrec:
            count=1
            server_index=0

    print index
    selected_server_ip = server[index]['ip']
    selected_server_mac = server[index]['mac']
    selected_server_outport = server[index]['outport']
    
    # Setup route to server
    msg.buffer_id = event.ofp.buffer_id
    msg.in_port = event.port

    msg.actions.append(of.ofp_action_dl_addr(of.OFPAT_SET_DL_DST, selected_server_mac))
    msg.actions.append(of.ofp_action_nw_addr(of.OFPAT_SET_NW_DST, selected_server_ip))
    msg.actions.append(of.ofp_action_output(port = selected_server_outport))
    event.connection.send(msg)

    # Setup reverse route from server
    reverse_msg = of.ofp_flow_mod()
    reverse_msg.buffer_id = None
    reverse_msg.in_port = selected_server_outport

    reverse_msg.match = of.ofp_match()
    reverse_msg.match.dl_src = selected_server_mac
    reverse_msg.match.nw_src = selected_server_ip
    reverse_msg.match.tp_src = msg.match.tp_dst

    reverse_msg.match.dl_dst = msg.match.dl_src
    reverse_msg.match.nw_dst = msg.match.nw_src
    reverse_msg.match.tp_dst = msg.match.tp_src

    reverse_msg.actions.append(of.ofp_action_dl_addr(of.OFPAT_SET_DL_SRC, virtual_mac))
    reverse_msg.actions.append(of.ofp_action_nw_addr(of.OFPAT_SET_NW_SRC, virtual_ip))
    reverse_msg.actions.append(of.ofp_action_output(port = msg.in_port))
    event.connection.send(reverse_msg)

    return EventHalt

def launch ():
    # To intercept packets before the learning switch
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn, priority=2)

    log.info("Stateless LB running.")
