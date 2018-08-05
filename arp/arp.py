import socket
import time
from uuid import getnode as get_mac
import header
import sys


sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW)

sock.bind((sys.argv[1],socket.SOCK_RAW))



