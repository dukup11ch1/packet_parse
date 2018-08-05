import socket
import time
import uuid
import header
import sys
import struct
import platform
import re
from getmac import get_mac_address

def ip2int(ip):
    ip.split('.')

interface=sys.argv[1]
sender_ip=sys.argv[2]
target_ip=sys.argv[3]
#mymac=get_mac(sys.argv[1])
mymac = get_mac_address(interface=interface)
#print win_mac 


myeth=header.Eth("\xff\xff\xff\xff"+mymac+"\x08\x06")
myarp=header.Arp("\x00\x01"+"\x08\x00"+"\x06\x04"+"\x01")