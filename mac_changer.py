#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface , new_mac):
    print(f"[+] Changing MAC of {interface} to  {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()
parser.add_option("-i","--interface" , dest="interface" , help="The interface for which the mac is being changed")
parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address")
(options, arguments) = parser.parse_args()
change_mac(options.interface,options.new_mac)




