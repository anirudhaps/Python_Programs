'''
1. Write a function called square that takes a parameter named t, which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
2. Add another parameter, named length, to square. Modify the body so length of
the sides is length , and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for length .
'''

from swampy.TurtleWorld import *
from sys import argv

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)
    

world = TurtleWorld()
bob = Turtle()
ray = Turtle()
l = int(argv[1])
square(bob,l)
#square(ray,l)
#wait_for_user()
