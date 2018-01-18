
def do_twice(f,val):
    f(val)
    f(val)
    
def print_val(v):
    print v
    print v

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

do_four(print_val,'pig')
