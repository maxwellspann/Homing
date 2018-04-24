#
# Mar02.py
# Martin Spann
# March 02, 2017
#
# SOCV pdf to usable data project

import os, xlrd

from xlutils.copy import copy

# Change to working directory
os.chdir("c:/Users/mspann/Documents/Pam/WorkingDirectory")

# Open the xlsx in the working dir
# This object is only readable
workbook = xlrd.open_workbook('2016.xlsx')

# Create a new file and make writable
wb = copy(workbook)

# inputsheet var holds the contents of the Input Tab
inputsheet = wb.get_sheet(0)

# outputcontainer var holds the contents of the third tab
outputcontainersheet = wb.get_sheet(2)

outputcontainersheet.write(0,1,'975423724597')


wb.save('2016a.xls')

# loop down the rows testing first column for the char 4
# Using 4 because it is in every vtds
# Don't have my if statement correct yet

#for row in range(inputsheet.nrows):
#    vtds = inputsheet.cell_value(row,0)
#    if 4 in vtds:
#        print(vtds)
