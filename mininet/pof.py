
from mininet.log import info, error, warn, debug
from mininet.util import ( quietRun, errRun, errFail, moveIntf, isShellBuiltin,
                           numCores, retry, mountCgroups )
from mininet.moduledeps import moduleDeps, pathCheck, OVS_KMOD, OF_KMOD, TUN
from mininet.link import Link, Intf, TCIntf
from mininet.node import Switch

class POFSwitch( Switch ):
    """POF virtual switch"""
    def __init__( self, name, **kwargs ):
        Switch.__init__( self, name, **kwargs )

    @classmethod
    def setup( cls ):
        "Make sure POFSwitch is installed"
        pathCheck( 'pofswitch', 
                    moduleName='POF Switch (poforwarding.org)')
        out, err, exitcode = errRun( 'pofswitch -h' )
        if exitcode:
            error( out + err +
                   'pofswitch exited with code %d\n' % exitcode )
            exit( 1 )
        
    def start( self, controllers ):
        "Start up a new POF Switch"
        info( 'Device ID=%s, ' % self.dpid )
        info( 'listen-port=%s\n' % self.listenPort )
        args = ['pofswitch']
#        for intf in self.intfs.values():
#            if not intf.IP():
#                args.extend( ['-i', intf.name] )
        args.extend( ['--verbosity=mute'] )
        args.extend( ['--promisc'] )
        for c in controllers:
            args.extend( ['--ip-addr=%s' % c.IP()] )
            args.extend( ['--port=%s' % c.port] )
        args.extend( ['--device-id=%s' % self.dpid] )
        for intf in self.intfList():
            if not intf.name == 'lo':
                args.extend( ['--add-port=%s' % intf] )
        args.extend( ['--log-file=/usr/local/var/log/pofswitch-mn-%s.log' % self.name] )
        if self.listenPort:
            args.extend( ['--listen-port=%i' % self.listenPort] )
        args.append( self.opts )

        self.cmd( 'ifconfig lo up' )
        self.cmd( ' '.join(args) + ' &')

    def stop( self ):
        "Terminate POF switch."
        self.cmd( 'killall pofswitch' )
        self.deleteIntfs()

    def attach( self, intf ):
        "Connect a data port"
#        self.cmd( 'ivs-ctl', 'add-port', '--datapath', self.name, intf )

    def detach( self, intf ):
        "Disconnect a data port"
#        self.cmd( 'ivs-ctl', 'del-port', '--datapath', self.name, intf )

    def dpctl( self, *args ):
        "Run dpctl command"
#        if not self.listenPort:
#            return "can't run dpctl without passive listening port"
#        return self.cmd( 'ovs-ofctl ' + ' '.join( args ) +
#                         ' tcp:127.0.0.1:%i' % self.listenPort )
