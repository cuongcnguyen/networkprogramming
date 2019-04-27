import socket
import datetime, time
from struct import unpack
from print_time import print_time

UDP_IP = '127.0.0.1'
UDP_PORT = 37
BUFFER_SIZE = 2048

mysocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.sendto(bytes(), (UDP_IP, UDP_PORT))

data = mysocket.recvfrom(BUFFER_SIZE)

time = unpack("!L", data[0])
time = time[0]
print("received data: " +  str(time))

print_time(time)