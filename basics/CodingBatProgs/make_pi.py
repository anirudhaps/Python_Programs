'''
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() -> [3, 1, 4]
'''
from math import pi

def make_pi():
    spi = str(pi)
    slst = list(spi)
    rlst = []
    rlst.append(int(slst[0]))
    rlst.append(int(slst[2]))
    rlst.append(int(slst[3]))
    return rlst

print make_pi()
