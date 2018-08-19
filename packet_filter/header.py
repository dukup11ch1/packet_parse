import struct
import socket

class Ip:
    def __init__(self,raw=None):
        iph=struct.unpack('!BBHHHBBH4s4s',raw[:20])
        self._version=iph[0]>>4
        self._ihl=iph[0]&0xF
        #iph_length=ihl*4
        self._ttl=iph[5]
        self._protocol=iph[6]
        self._srcip=socket.inet_ntoa(iph[8])
        self._dstip=socket.inet_ntoa(iph[9])

    def version(self):
        return self._version

    def iph_length(self):
        return self._ihl

    def ttl(self):
        return self._ttl

    def protocol(self):
        return self._protocol

    def srcip(self):
        return self._srcip

    def dstip(self):
        return self._dstip

class Tcp:
    def __init__(self,raw=None):
        ipl=Ip(raw).iph_length()*4
        tcph=struct.unpack('!HHLLBBHHH',raw[ipl:ipl+20])
        self._srcport=tcph[0]
        self._dstport=tcph[1]
        self._seq=tcph[2]
        self._ack=tcph[3]
        self._reserved=tcph[4]
        self._hlen=tcph[4]>>4
        self._data=raw[ipl+self._hlen*4:]
    
    def srcport(self):
        return self._srcport
    
    def dstport(self):
        return self._dstport
    
    def sequence(self):
        return self._seq
    
    def acknowledgment(self):
        return self._ack
    
    def header_len(self):
        return self._hlen
    
    def data(self):
        return self._data