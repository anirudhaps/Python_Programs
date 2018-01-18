from sys import argv

def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)
    
def printHello():
    print 'hello'

no = int(argv[1])
do_n(printHello,no)
