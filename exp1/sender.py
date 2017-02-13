from socket import *
import sys
import select
from time import time

address = ('10.0.0.2', 1567)
client_socket = socket(AF_INET, SOCK_DGRAM)

seq = 0

print "Sending packets to host2..."
print "Saving files to log..."

i = 0

logfile = open("sender log.txt","w")

while True:
	seq+=1
	data = "%d"%i
	t = time()
	client_socket.sendto(data, address)
	log = "Sending packet #%d to host2... (timestamp=%.10f)" % (i,t)
	logfile.write('%s\n'%log)
	print log
	i+=1

client_socket.close()