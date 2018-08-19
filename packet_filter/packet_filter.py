import socket
import sys
import header

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    s.bind((sys.argv[1],0))
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

while True:
    packet = s.recvfrom(65565)
    packet = packet[0]
    head = header.Tcp(packet)
    if head.dstport()==80:
        try:
            if head.data().split()[4]==sys.argv[2]:
                print "block"
        
        except:
            pass