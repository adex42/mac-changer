#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface" , dest="interface" , help="The interface for which the mac is being changed")
parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address")
(options, arguments) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac
print("[+] MAC before change")
subprocess.call(["ifconfig", interface])
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] MAC after the Change")
subprocess.call(["ifconfig", interface])


