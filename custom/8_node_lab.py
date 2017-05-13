from mininet.topo import Topo

class MyTopo (Topo):
    "8-node SDN lab network."
    def __init__(self):
        #Initialize topology
        Topo.__init__(self)

        "Creating switches..."
        s_114 = self.addSwitch('s_114')
        s_115 = self.addSwitch('s_115')
        s_116 = self.addSwitch('s_116')
        s_117 = self.addSwitch('s_117')
        s_120 = self.addSwitch('s_120')
        s_121 = self.addSwitch('s_121')
        s_122 = self.addSwitch('s_122')
        s_123 = self.addSwitch('s_123')

topos = { '8_node_lab': (lambda: MyTopo()) }
