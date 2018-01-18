'''
3. The functions lt and rt make 90-degree turns by default, but you can provide a
second argument that specifies the number of degrees. For example, lt(bob, 45)
turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon . Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
'''

from swampy.TurtleWorld import *
from sys import argv

def polygon(t,length,n,nums):
    deg = 360.0/n
    for i in range(nums):
        fd(t,length)
        lt(t,deg)

def circle(t,r):
    polygon(t,r,360,60)
    
def arc(t,r,angle):
    polygon(t,r,360,angle)
    
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
r = int(argv[1])
an = int(argv[2])
#polygon(bob,l,no)
arc(bob,r,an)
wait_for_user()
