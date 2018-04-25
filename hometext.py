#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:45:06 2018

@author: Maxwell Francisco Spann
"""

import sys

filename = sys.argv[1]
hostnum = int(sys.argv[2])

file = open(filename, "r")
for line in file:
   x = line.rstrip()
   f = open("sh-172.23.1.%s" % hostnum, "w+")
   f.write("host sh-172-23-1-%s { \n hardware ethernet %s; \n fixed-address 172.23.1.%s;\n }"  % ( hostnum, x, hostnum ))
   f.close()
   hostnum = hostnum + 1
  

 
