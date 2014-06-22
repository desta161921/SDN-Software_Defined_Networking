#__author__ = 'desta'
#!/usr/bin/python

'''
Custom Topology
Created by: Desta Haileselassie Hagos
'''

from mininet.topo import Topo
from mininet.util import irange, dumpNodeConnections
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import CPULimitedHost
from mininet.log import setLogLevel

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Here are my logics
        self.fanout = fanout
        self.linkopts1 = linkopts1
        self.linkopts2 = linkopts2
        self.linkopts3 = linkopts3

        coreSwitch = self.addSwitch('c1')
        for x in irange(1,fanout):
        	Aggregation = self.addSwitch('a%s' % x)
        	self.addLink(coreSwitch, Aggregation, **linkopts1)
        	for y in irange(1,fanout):
        		Edge = self.addSwitch('e%s' % (fanout * (x - 1) + y ))
        		self.addLink(Aggregation, Edge, **linkopts2)
        		for z in irange(1,fanout):
        			Host = self.addHost('h%s' % ((fanout * (fanout*(x - 1) + y - 1)) + z))
        			self.addLink(Edge, Host, **linkopts3)

def perfTest():
	"Create a network and run simle performance test"
	linkopts1 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
	linkopts2 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
	linkopts3 = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
	topo =  CustomTopo(linkopts1, linkopts2, linkopts3, fanout=2)
	net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)

	#Start the network
	net.start()
	print "Dumping host dumpNodeConnections"
	dumpNodeConnections(net.hosts)
	print "Testing network connetivity"
	net.pingAll()
	print "Testing bandwidth between hosts h1 and h4"
	h1, h4 = net.get('h1', 'h4')
	net.iperf((h1, h4))
	#Call ineractive CLI
	#mininet.cli.CLI(net)

	net.stop()
if __name__ == '__main__':
        #Tell mininet to print useful information
        setLogLevel('info')
        perfTest()

topos = { 'custom': ( lambda: CustomTopo() ) }
