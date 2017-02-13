class NetworkGraph:

	def __init__(self):
		self.edges = {} # edges[switch_dpid] = set( (nextdpid, fwdport )  )
		self.hosts = set()
		self.port_to_connectedendpoints = {}

		self.portUsage = {} # portUsage[switch][port] = "M" or "B" for main and backup path
		self.cntGrpTable = {} #cntGrpTable[switch] = total group tables in switch
		return


	def addEdge(self, src, dst, fwdport):
		if src not in self.edges: self.edges[src] = set()
		if src not in self.cntGrpTable: self.cntGrpTable[src]=0
		if src not in self.portUsage: self.portUsage[src]={}
		self.portUsage[src][fwdport] = "B"

		self.edges[src].add( (dst,fwdport) )
		return


	def addHost(self,hostip):
		self.hosts.add(hostip)
		return



	def removeEdge(self, src, dst, fwdport):
		self.edges[src].remove( (dst,fwdport) )
		return

	def recognizeHost(self, host):
		if host in self.hosts: return True
		return False

	def getShortestPath(self, src, dst):
		import Queue
		Q = Queue.Queue(maxsize = 0)
		Q.put( (src,-1) )
		visited = {}
		pushed = {}
		pushed[src]=True
		parent = {}
		while True:
			curnode,curfwdport = Q.get()
			if curnode in visited: continue
			visited[curnode]=True

			if curnode==dst:
				break

			for edge in self.edges[curnode]:
				nextnode,nextfwdport = edge
				if nextnode in pushed: continue
				pushed[nextnode]=True
				Q.put( (nextnode,nextfwdport) )
				parent[ nextnode ] = (curnode,nextfwdport)

		path = [(dst,-1)]
		# for key in parent:
		# 	print key
		# 	print parent[key]
		curr = dst
		while curr in parent:
			path = [parent[curr]]+path
			curr,x = parent[curr]

		for s,p in path:
			if s not in self.port_to_connectedendpoints: self.port_to_connectedendpoints[s] = {}
			if p not in self.port_to_connectedendpoints[s]: self.port_to_connectedendpoints[s][p] = set()
			self.port_to_connectedendpoints[s][p].add( (src,dst) )
		return path

	def findMiddleNode(self,dpid1,dpid2):
		for n,p in self.edges[dpid1]:
			for nn,pp in self.edges[dpid2]:
				if n==nn: return n
		return None

	def findFwdPort(self,dpid1,dpid2):
		for nxt,port in self.edges[dpid1]:
			if nxt == dpid2: return port
		return None

	def getConnectedEndpoints(self,dpid, port):
		if dpid not in self.port_to_connectedendpoints: return None
		if port not in self.port_to_connectedendpoints[dpid]: return None
		return self.port_to_connectedendpoints[dpid][port]

	def incGroupCount(self,dpid):
		self.cntGrpTable[dpid]+=1
		return self.cntGrpTable[dpid]

	


