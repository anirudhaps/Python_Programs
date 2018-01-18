'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) -> True
make_bricks(3, 1, 9) -> False
make_bricks(3, 2, 10) -> True
'''
from sys import argv

def make_bricks(small,big,goal):
    n5 = goal/5
    if big>=n5:
        goal = goal - 5 * n5
    else:
        goal = goal - 5 * big
    
    if small>=goal:
        return True
    else:
        return False
        
s = int(argv[1])
b = int(argv[2])
g = int(argv[3])
print make_bricks(s,b,g)
