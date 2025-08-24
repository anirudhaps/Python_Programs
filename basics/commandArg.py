#command line arguments in python

import sys
print (sys.argv)       # argv is the list name used for command-line arguments
print (sys.argv[0])    # python program name
print (sys.argv[1])    # 1st command line argument
print (sys.argv[2])    # 2nd command line argument
print (len(sys.argv))

print ('All command line arguments alongwith the program name:')
i=0
while i<len(sys.argv):
    print (sys.argv[i])
    i=i+1
