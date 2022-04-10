#!/usr/bin/python

"""
This setup the topology in lab3-part1
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.link import Link, Intf, TCLink
import os 
from time import sleep
import sys

class Topology(Topo):
    
    
    def __init__(self):
        "Create Topology."
        
        # Initialize topology
        Topo.__init__(self)
        
        
        #### There is a rule of naming the hosts and switch, so please follow the rules like "h1", "h2" or "s1", "s2" for hosts and switches!!!!
      
        # Add hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        
        # Add switches
        sw1 = self.addSwitch('s1')
        sw2 = self.addSwitch('s2')
        sw3 = self.addSwitch('s3')
        sw4 = self.addSwitch('s4')
        
        self.addLink(host1, sw1, 1, 1)
        self.addLink(host2, sw2, 1, 1)
        self.addLink(host3, sw3, 1, 1)
        self.addLink(host4, sw4, 1, 1)
        self.addLink(sw1, sw2, 2, 3)
        self.addLink(sw2, sw3, 2, 3)
        self.addLink(sw3, sw4, 2, 3)
        self.addLink(sw4, sw1, 2, 3)
        
        

# This is for "mn --custom"
topos = { 'mytopo': ( lambda: Topology() ) }




# This is for "python *.py"
if __name__ == '__main__':
    setLogLevel( 'info' )
            
    topo = Topology()
    net = Mininet(topo=topo, link=TCLink)       # The TCLink is a special setting for setting the bandwidth in the future.
    
    # 1. Start mininet
    net.start()
    
    
    # Wait for links setup (sometimes, it takes some time to setup, so wait for a while before mininet starts)
    print "\nWaiting for links to setup . . . .",
    sys.stdout.flush()
    for time_idx in range(3):
        print ".",
        sys.stdout.flush()
        sleep(1)
    
        
    # 2. Start the CLI commands
    info( '\n*** Running CLI\n' )
    CLI( net )
    
    
    # 3. Stop mininet properly
    net.stop()


    ### If you did not close the mininet, please run "mn -c" to clean up and re-run the mininet 
