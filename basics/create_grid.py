import sys

def create_grid(n):
    '''creates a n by n grid'''
    ph = '+----'
    vs = '|    '
    hori1 = ph * n + '+'
    hori2 = vs * n + '|'
    i = 0
    while i<n:
        print(hori1)
        j=0
        while j<4:
            print(hori2)
            j+=1
        i+=1
    print(hori1)
    
if __name__ == '__main__':
    create_grid(int(sys.argv[1]))
