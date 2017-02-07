from socket import *
import sys
import select
from time import time

print "Receiving packets from host1"
address = ('10.0.0.2', 1567)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

time_last_packet = time()

avg_interval = 0

logfile = open("receiver log.txt","w")

while True:
    recv_data, addr = server_socket.recvfrom(2048)
    time_new_packet = time()
    interval = time_new_packet - time_last_packet
    avg_interval+=interval
    avg_interval/=2
    log = "Packet %d Received from host1 at %.10f! Time taken=%.10f Avg=%.10f" % (int(recv_data),time_new_packet,interval,avg_interval)
    print log
    logfile.write(log+"\n")
    time_last_packet = time_new_packet
    

server_socket.close()