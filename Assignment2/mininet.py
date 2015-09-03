#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""
import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    
    num_switch = int(sys.argv[1])
    num_host = int(sys.argv[2])
    total_host = num_switch*num_host

    odd_ip = '10.0.0.'
    even_ip = '11.0.0.'

    list_oddhosts = []
    list_evenhosts = []

    for i in range(total_host):
	    host_name = 'h'+str(i)
    	if i % 2 == 0:
		    add = net.addHost(host_name, ip=even_ip+str(i+1))
		    list_evenhosts.append(add)
	  else:
		  add = net.addHost(host_name, ip=odd_ip+str(i+1))
		  list_oddhosts.append(add)

    #info( '*** Adding hosts\n' )
    #h1 = net.addHost( 'h1', ip='10.0.0.1' )
    #h2 = net.addHost( 'h2', ip='10.0.0.2' )

    info( '*** Adding switch\n' )
    #s1 = net.addSwitch( 's1' )
    #s2 = net.addSwitch( 's2' )
    list_switch = []
    for i in range(num_switch):
	    s = 's'+str(i)
	    switch = net.addSwitch(s)
	    list_switch.append(switch)

    info( '*** Creating links\n' )
    #net.addLink( h1, s3 )
    #net.addLink( h2, s3 )

    k = 0
    for i in list_switch:
	    net.addLink(list_oddhosts[k], i)
	    net.addLink(list_evenhosts[k], i)
	    k = k + 1

    for i in range(len(list_switch)-1):
	    net.addLink(list_switch[i], list_switch[i+1])
    

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
