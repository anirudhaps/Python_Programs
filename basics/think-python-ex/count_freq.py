'''
Count the frequency of each character in a string
Exercise 11-3
'''
from sys import argv

def count_freq(dstr):
    d = dict()
    for c in dstr:
        d[c] = d.get(c,0)+1 # get method takes a key(c) and default value. If c is in d, get returns the value of it. Otherwise, it returns
        #if c in d:         # the default value(0 in our case)
            #d[c]+=1
        #else:
            #d[c]=1
    return d

def print_dict(dc):
    l = dc.keys()
    for k in sorted(l):
        print k, dc[k]

#h = count_freq(argv[1])
#print_dict(h)
