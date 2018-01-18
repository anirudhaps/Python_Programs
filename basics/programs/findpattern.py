# finding a particular pattern in the file
# filename and pattern are input as commandline arguments

import sys
import re

def Find(pat, text):
    m = re.search(pat,text)  # m = None or empty string or 0 will be taken as false
    if m:
        return True
    else:
        return False

p = sys.argv[1]  # 1st commandline argument is pattern
fn = sys.argv[2] # 2nd commandline argument is filename

f = open(fn,'r')
k=0
for line in f:
    o = Find(p,line)
    if o:
        print 'patten exists in the file'
        k=1
        break

if k==0:
    print 'pattern not found'
f.close()


