#!/usr/bin/env python

import subprocess

interface = input("interface >> ")
new_mac = input("new mac >> ")
print("[+] MAC before change")
subprocess.call(["ifconfig", interface])
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] MAC after the Change")
subprocess.call(["ifconfig", interface])


