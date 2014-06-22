#__author__ = 'desta'
#!/usr/bin/python

'''
Linear Topology Test

Created by: Desta Haileselassie Hagos
'''

from mininet.net import Mininet
from mininet.topo import LinearTopo

Linear=LinearTopo(k=4)
net=Mininet(topo=Linear)

net.start()
net.pingAll()
net.stop()
