'''
Command Receiver
Created on Jul 2, 2019

@author: Tyler Andjel
'''

import sys
from socket import socket, AF_INET, SOCK_DGRAM

# CMD Setup
IED_ON            = "IDN"
IED_OFF           = "IDF"
SHUTDOWN_ROVER    = "SF"
LEFT_FORK_LEFT    = "LFL"
LEFT_FORK_CENTER  = "LFC"
LEFT_FORK_UP      = "LFU"
LEFT_FORK_DOWN    = "LFD"
RIGHT_FORK_RIGHT  = "RFR"
RIGHT_FORK_CENTER = "RFC"
RIGHT_FORK_UP     = "RFU"
RIGHT_FORK_DOWN   = "RFD"
EXIT              = "EXIT"

# Network Setup
host = "127.0.0.1"
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

print("Waiting to receive messages...")
while True:
    (cmd, addr) = UDPSock.recvfrom(buf)
    # Decode command sent
    cmd = cmd.decode();
    print("Received message: " + cmd)
    if cmd == IED_ON:
        print(IED_ON)
    elif cmd == IED_OFF:
        print(IED_OFF)
    elif cmd == SHUTDOWN_ROVER:
        print(SHUTDOWN_ROVER)
    elif cmd == LEFT_FORK_LEFT:
        print(LEFT_FORK_LEFT)
    elif cmd == LEFT_FORK_CENTER:
        print(LEFT_FORK_CENTER)
    elif cmd == LEFT_FORK_UP:
        print(LEFT_FORK_UP)
    elif cmd == LEFT_FORK_DOWN:
        print(LEFT_FORK_DOWN)
    elif cmd == RIGHT_FORK_RIGHT:
        print(RIGHT_FORK_RIGHT)
    elif cmd == RIGHT_FORK_CENTER:
        print(RIGHT_FORK_CENTER)
    elif cmd == RIGHT_FORK_UP:
        print(RIGHT_FORK_UP)
    elif cmd == RIGHT_FORK_DOWN:
        print(LEFT_FORK_DOWN)
    elif cmd == EXIT:
        break
UDPSock.close()
sys.exit()