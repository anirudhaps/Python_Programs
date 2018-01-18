

def check_fermat(a,b,c,n):
    lh = a**n + b**n
    rh = c**n
    if n>2:
        if lh==rh:
            print 'Holy smokes, Fermat was wrong!'
        else:
            print 'No, that doesn\'t work'

va = int(raw_input('a='))
vb = int(raw_input('b='))
vc = int(raw_input('c='))
vn = int(raw_input('n='))

check_fermat(va,vb,vc,vn)
