'''
Exercise-7.4
'''
import math

def eval_loop():
    ex = raw_input('>')
    while ex!='done':
        val = eval(ex)
        print val
        ex = raw_input('>')
    return val

if __name__=='__main__':
    r = eval_loop()
    print r
