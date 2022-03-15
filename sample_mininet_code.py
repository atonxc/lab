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
        host1 = self.addHost('h1', ip='10.0.0.1/24')
        host2 = self.addHost('h2')
        
        
        # Add switches
        swA = self.addSwitch('s1')
        swB = self.addSwitch('s2')
        swC = self.addSwitch('s3')
        swD = self.addSwitch('s4')
        swE = self.addSwitch('s5')
        
        
        self.addLink(host1, swA)
        self.addLink(swA, swB, 2, 2)    # Connect port 1 of switch A with port 2 of switch B
        self.addLink(swA, swC)
        self.addLink(swB, swE)
        self.addLink(swE, swC)
        self.addLink(swC, swD)
        self.addLink(swD, host2)
        

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
