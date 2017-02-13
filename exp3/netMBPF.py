from time import sleep,time
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from CustomTopology import createTopology
from mininet.node import RemoteController
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

#####ADD The REMOTE CONTROLLER########
network.addController(name='c0',controller=RemoteController)

#####START THE NETWORK########
network.start()
print "network has started..."

#####INSTALL ARP ENTRIES########
h1.setMAC('00:00:00:00:00:01',intf='h1-eth0')
h2.setMAC('00:00:00:00:00:02',intf='h2-eth0')
#h1 and h2 should know each other's arp entries
h1.setARP('10.0.0.2','00:00:00:00:00:02');
h2.setARP('10.0.0.1','00:00:00:00:00:01');

#####WAIT FOR THE CONTROLLER TO LEARN THE NETWORK########
sleep(8.0)

#####H2 TELLS CONTROLLER ABOUT ITS EXISTENCE########
h2.cmd('ping -c1 -W 1 10.0.0.1')
print "Everything ready!!"



#####WAIT UNTIL THE PING IS SUCCESSFULL########
myutil.waitFor1stSuccessfulPing(h1, '10.0.0.2')

#####SAVE INITIAL FLOW TABLES IN FILES########
print "Writing the flow entries to files..."
for switch in switches:
	result = switch.cmd('ovs-ofctl dump-flows',switch)
	open('InitialFlowTable_%s.txt'%switch,'w').write(result)

CLI(network)

#####SAVE MODIFIED FLOW TABLES IN FILES########
print "Writing the flow entries to files..."
for switch in switches:
	result = switch.cmd('ovs-ofctl dump-flows',switch)
	open('ModifiedFlowTable_%s.txt'%switch,'w').write(result)

#####STOP THE NETWORK########

network.stop()