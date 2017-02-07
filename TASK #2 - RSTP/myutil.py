def isUnsuccessfulPing(pingresult):
	if '+1 errors' not in pingresult and '100% packet loss' not in pingresult and 'Destination Host Unreachable' not in pingresult:
		return False
	else:
		return True


def waitFor1stSuccessfulPing(host, dest_ip):
	while True:
		pingresult = host.cmd('ping -c1 -W 1 %s' % dest_ip)
		if not isUnsuccessfulPing(pingresult):
			return