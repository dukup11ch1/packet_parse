import socket
import sys
import header
import pydivert

w = pydivert.WinDivert()
w.open()

while True:
    
    packet,recv_len,address = w.recv()
    #print packet
    head = header.Tcp(packet)
    if head.dstport()==80:
        try:
            if head.data().split()[4] in sys.argv:
                print "block!"
                continue
        
        except:
            pass

    w.send(packet,recv_len,address)
w.close()