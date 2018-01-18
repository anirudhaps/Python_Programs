'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) -> 4
make_chocolate(4, 1, 10) -> -1
make_chocolate(4, 1, 7) -> 2
'''

from sys import argv

def make_chocolate(small,big,goal):
    n5 = goal/5
    if big>=n5:
        goal = goal - 5 * n5
    else:
        goal = goal - 5 * big
    
    if small>=goal:
        return goal
    else:
        return -1
        
s = int(argv[1])
b = int(argv[2])
g = int(argv[3])
print make_chocolate(s,b,g)
