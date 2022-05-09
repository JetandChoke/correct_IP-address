#!/usr/bin/env/python3
from netaddr import *
import ipaddress
import re
import fileinput
import pdb

## Runs through the file looking for ip-addresses. If address is found, changes all host addresses (non-zero host bit) to network  addresses from the specified subnet.
## Simply useful for ACL/Traffic-Policy config files modifications.

# file = input('Enter filename: ')
file = 'ip.txt'

with fileinput.FileInput(file, inplace=True, backup='.bak') as f:
    for line1 in f:
        line = line1.split()
        # print(line)
        for elem in line:
            # pdb.set_trace()
            # print(f'working on: ', elem)
            if elem[0].isdigit():
                # print(f'elem starts with a digit: ', elem)
                try:
                    # check if elem is IP or not
                    int_sub = ipaddress.ip_network(elem, strict=False)
                    # print(f'compare elem: {elem} and int_sub: {int_sub}')
                    if str(elem) != str(int_sub):
                        # print(f'elem is subnet, skipping... ', elem)
                        # print(f'changing {elem} to {int_sub}...')
                        line1=line1.replace(elem, str(int_sub))
                        # print(line1)
                    # else:
                        # print(f'elem is subnet, skipping... ', elem)
                except ValueError:
                    # print(f'already a network: ', elem)
                    continue
        print(line1, end='')
        
        
