'''
First step towards exception handling
'''

try:
    fin = open('frequent.txt')
    for l in fin:
        print l
    fin.close()
except:
    print 'Something went wrong'
