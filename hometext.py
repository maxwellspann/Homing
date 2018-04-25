#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:45:06 2018

@author: Maxwell Francisco Spann
"""

import sys

filename = sys.argv[1]
hostnum = sys.argv[2]

file = open(filename, "r")
for line in file:
   print line,

f= open("sh-172.23.1.%s" % hostnum, "w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()

 
