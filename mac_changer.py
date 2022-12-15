#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface for which the mac is being changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter an interface to use , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please enter an mac to use , use --help for more info")
    return options

def change_mac(interface , new_mac):
    print(f"[+] Changing MAC of {interface} to  {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface,options.new_mac)




