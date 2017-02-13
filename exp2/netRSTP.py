from time import time
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from CustomTopology import createTopology
import myutil
print "imported necessery files..."

#####CREATE THE NETWORK########
network = Mininet(link=TCLink)
print "network created..."

#####CREATE THE TOPOLOGY########
nodes = createTopology(network)
hosts = nodes["hosts"]
switches = nodes["switches"]
h1,h2 = hosts[0],hosts[1]
s1,s2,s3 = switches[0],switches[1],switches[2]
s4,s5,s6 = switches[3],switches[4],switches[5]
s7 = switches[6]


#####START THE NETWORK########
network.start()
print "network has started..."

#####ENABLE RSTP########
print "enabling rapid spanning tree protocol..."
for switch in switches:
	switch.cmd( 'ovs-vsctl set-fail-mode', switch , 'standalone' ) #LEARNS MAC
	switch.cmd('ovs-vsctl set Bridge', switch , 'rstp_enable=true') #STP


#####WAIT FOR STP TO CONVERGE########
t0 = time()
myutil.waitFor1stSuccessfulPing(h1,'10.0.0.2')
t1 = time()
print "rapid spanning tree protocol has been enabled (time taken= %ss)..."%(t1-t0)


#####CONTROL TO THE COMMAND LINE INTERFACE########
CLI(network)

#####STOP THE NETWORK########
network.stop()