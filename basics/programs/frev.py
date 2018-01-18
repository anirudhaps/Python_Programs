#find and reverse a substring
#check whether a string substr is found in parent string mnstr.
#If yes, then within the mnstr, reverse that substring part.

def frev(mnstr,substr):
    ind = mnstr.find(substr)
    if ind!=-1:
        ms = list(mnstr)
        l = len(substr)
        k = ms[ind:ind+l]        
        k.reverse()        
        ms[ind:ind+l] = k
        delim = ''
        mnstr = delim.join(ms)
        print 'The substring is found in main string!'
        print 'main string with reverse substring contained in it: ' + mnstr
    else:
        print 'The substring is not found in main string!'


main = raw_input('Enter parent string: ')
child = raw_input('Enter child string: ')
frev(main,child)
