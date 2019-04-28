import socket
import datetime, time
from struct import unpack
from print_time import print_time

mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("127.0.0.1", 37))


data = mysocket.recv(2048)
data= int.from_bytes(data, byteorder="big")

mysocket.send(b"Connected to the client. Data sent.")
mysocket.close()

print (data)

print_time(data)
