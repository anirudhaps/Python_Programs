'''
Exercise 14-2: sed
'''

def sed(pattern,replacement,file1,file2):
    try:
        fn1 = open(file1)
        fn2 = open(file2,'w')
        for line in fn1:            
            if pattern in line:
                line = line.replace(pattern,replacement)
            fn2.write(line)
        fn2.close()
        fn1.close()
    except:
        print 'Error during execution: something went wrong'

fname1 = raw_input('Enter filename-1: ')
fname2 = raw_input('Enter filename-2: ')
sed('2','raj',fname1,fname2)
