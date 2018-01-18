'''
walk through the directory
'''
import os

def walk(dirname):
    dlist = os.listdir(dirname)
    directories = []
    print os.path.abspath(dirname) + ':'
    for d in dlist:
        if os.path.isdir(d):
            directories.append(d)
        else:
            print d
    
    if directories==[]:
        return
    
    for d in directories:
        walk(d)

cwd = os.getcwd()
walk(cwd)
