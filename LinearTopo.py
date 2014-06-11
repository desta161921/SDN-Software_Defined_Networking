#__author__ = 'desta'

#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
import mininet.util

class LinearTopo(Topo):
   "Linear topology of k switches, with one host per switch."

   def __init__(self, k = 2, **opts):
       """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

       super(LinearTopo, self).__init__(**opts)

       self.k = k

       lastSwitch = None
       for i in irange(1,k):
       	host = self.addHost('h%s' % i)
       	switch = self.addSwitch('s%s' % i)
       	#self.addLink(host, switch)
       	#10 Mbps, 5ms delay, 1% loss, 1000 packet queue
       	self.addLink(host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)

       	if lastSwitch:
       		self.addLink(switch, lastSwitch)
       	lastSwitch = switch
def perfTest():
	"Create a network and run simle performance test"
	topo = LinearTopo(k=4)
	#net = Mininet(topo)
	net=Mininet(topo=topo, host=CPULimitedHost,link=TCLink)
	net.start()

	print "Dumping host connections"
	dumpNodeConnections(net.hosts)
	print "Testing network cnonnectivity"
	net.pingAll()
	print "Testing bandwidth between h1 and h4"
	h1, h4=net.get('h1', 'h4')
	net.iperf((h1, h4))
	# Call ineractive CLI
	mininet.cli.CLI(net)
	net.stop()
if __name__ == '__main__':
        #Tell mininet to print useful information
        setLogLevel('info')
        perfTest()
        
        