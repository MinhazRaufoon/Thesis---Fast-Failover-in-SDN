def createTopology(network=None):
	
	if network==None: return
	
	high_link_capacity=1000;
	medium_link_capacity=100
	low_link_capacity=10


	#adding hosts
	h1 = network.addHost('h1')
	h2 = network.addHost('h2')

	#adding switches
	s1 = network.addSwitch('s1')
	s3 = network.addSwitch('s3')
	s5 = network.addSwitch('s5')

	s2 = network.addSwitch('s2')
	s4 = network.addSwitch('s4')
	s6 = network.addSwitch('s6')

	s7 = network.addSwitch('s7')

	#adding links
	network.addLink(s1,h1,bw=low_link_capacity)
	network.addLink(s2,h2,bw=low_link_capacity)

	network.addLink(s1,s3,bw=medium_link_capacity)
	network.addLink(s2,s4,bw=medium_link_capacity)
	network.addLink(s1,s5,bw=low_link_capacity)
	network.addLink(s2,s6,bw=low_link_capacity)

	network.addLink(s3,s4,bw=medium_link_capacity)
	network.addLink(s4,s6,bw=medium_link_capacity)
	network.addLink(s6,s5,bw=medium_link_capacity)
	network.addLink(s5,s3,bw=medium_link_capacity)

	network.addLink(s7,s3,bw=high_link_capacity)
	network.addLink(s7,s4,bw=high_link_capacity)
	network.addLink(s7,s5,bw=high_link_capacity)
	network.addLink(s7,s6,bw=high_link_capacity)

	#set IP addresses
	h1.setIP('10.0.0.1')
	h2.setIP('10.0.0.2')

	nodes = {}
	nodes['hosts'] = [h1,h2]
	nodes['switches'] = [s1,s2,s3,s4,s5,s6,s7]

	return nodes



