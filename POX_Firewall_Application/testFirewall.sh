#__author__ = 'desta'
#!/usr/bin/python

'''
script

Created by: Desta Haileselassie Hagos
'''
pkill python

cp firewall.py ~/pox/pox/misc
cp firewall-policies.csv ~/pox/pox/misc
python ~/pox/pox.py forwarding.l2_learning misc.firewall &
sudo mn --topo single,3 --mac --switch ovsk --controller remote
