import socket
import datetime, time
from our_time import get_time_in_bin

dts = datetime.datetime.utcnow()
epochtime1 = round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
epochtime= epochtime1 + 2208988800

print("Server initiated")
print("Listening")

mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mysocket.bind(("127.0.0.1", 37))

while 1:
    data, addr = mysocket.recvfrom(2048)

    if data != bytes(): break
    print('Connection address: ' + addr[0] + " and port: " + str(addr[1]))
    print("received data:", data)
    mysocket.sendto(get_time_in_bin(), addr)