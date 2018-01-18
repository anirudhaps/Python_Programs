# regular expressions

import re

fl = open('f1.txt','r')
for t in fl:
    t = t.rstrip()
    if re.search('^Hello',t):
        print t
    print re.findall('^Hello',t)    
    
