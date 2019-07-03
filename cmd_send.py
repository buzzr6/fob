'''
Command Sender
Created on Jul 2, 2019

@author: Tyler Andjel
'''

import sys
from socket import socket, AF_INET, SOCK_DGRAM

# Get first argument
cmd = sys.argv[1] 

# Network Setup
host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

# Send command
UDPSock.sendto(cmd.encode(), addr)
UDPSock.close()
sys.exit()