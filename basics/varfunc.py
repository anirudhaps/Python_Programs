# passing variable number of arguments to a function

def varfunc(*para):
    print para   #para will be a tuple
    print 'Arguments passed:'
    for a in para:
        print a

def varfunc2(string,*para):
    print string, para

    
varfunc(1)
varfunc(1,2)
varfunc()
varfunc(1,2,'Hello')

varfunc2('single no. :',1)
varfunc2('Multiple nos: ',1,2)
varfunc2('No nos: ')
varfunc2('Multiple nos and greeting: ',1,2,'Hello')

# *para dictate that whatever set of arguments we pass, they become a tuple
# whose name will be para
