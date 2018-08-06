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
    ip=ip.split('.')
    realip=0
    for i in range(len(ip)):
        realip=realip+int(ip[i])*(256**(3-i))
    return realip
def mac2int(mac):
    mac=mac.split(":")
    realmac=0
    for i in range(len(mac)):
        realmac=realmac+int(mac[i])*(256**(5-i))

interface=sys.argv[1]
sender_ip=sys.argv[2]
target_ip=sys.argv[3]
target_mac=sys.argv[4] #추후수정 예정
#mymac=get_mac(sys.argv[1])
mymac = get_mac_address(interface=interface)
#target_mac=""
#print win_mac 
sender_ip=ip2int(sender_ip)
target_ip=ip2int(target_ip)

myeth=header.Eth("\xff\xff\xff\xff"+struct.pack('!6B',mymac)+"\x08\x06")
myarp=header.Arp("\x00\x01"+"\x08\x00"+"\x06\x04"+"\x01"+struct.pack('!6B',mymac)+struct.pack('!4B',sender_ip)+"\x00\x00\x00\x00\x00\x00"+struct.pack('!4B',target_ip))
s=socket(AF_PACKET,SOCK_RAW)
s.bind((interface,0))
s.send(myeth+myarp)