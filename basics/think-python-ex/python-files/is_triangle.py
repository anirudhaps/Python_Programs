def is_triangle(a,b,c):
    if (a+b)<c or (b+c)<a or (a+c)<b:
        print 'No'
    else:
        print 'Yes'
        
def tcheck():
    a = int(raw_input('a='))
    b = int(raw_input('b='))
    c = int(raw_input('c='))
    is_triangle(a,b,c)

if __name__=='__main__':
    tcheck()
