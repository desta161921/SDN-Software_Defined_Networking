#__author__ = 'desta'
#!/usr/bin/python

'''
Custom Mininet
Created by: Desta Haileselassie Hagos
'''
from mininet.net import Mininet
from mininet.topo import LinearTopo
import mininet.util #import all #createLink
net = Mininet()

# Creating nodes in the network
c0 = net.addController()
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')

# Creating links between nodes in the network
net.addLink(h3,s1)
net.addLink(h4,s1)
net.addLink(s1,s2)
net.addLink(h5,s2)

# INterface IP address configuration
h3.cmd('ifconfig h3-eth0 192.168.1.3 netmask 255.255.255.0 up')
h4.cmd('ifconfig h4-eth0 192.168.1.4 netmask 255.255.255.0 up')
h5.cmd('ifconfig h5-eth0 192.168.1.5 netmask 255.255.255.0 up')
s1.setIP('192.168.1.101','24')
s2.setIP('192.168.1.102','24')

# network Launching & control
net.start()
net.pingAll()

# Call ineractive CLI
mininet.cli.CLI(net)
net.stop()