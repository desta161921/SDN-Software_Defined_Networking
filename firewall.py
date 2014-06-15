#__author__ = 'desta'
#!/usr/bin/python

'''
Layer-2 Firewall Application

Created by: Desta Haileselassie Hagos
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''
fileEntry = []
with open(policyFile) as fileOpen:
    next(fileOpen) 
    csv_entry = csv.reader(fileOpen, delimiter=',')
    for numRows in csv_entry:
        fileEntry.append(numRows[1:])


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        for pairs in fileEntry:
            m = of.ofp_match()
            m.dl_src = EthAddr(pairs[0])
            m.dl_dst = EthAddr(pairs[1])
            msg = of.ofp_flow_mod()
            msg.match = m
            event.connection.send(msg)
        
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
