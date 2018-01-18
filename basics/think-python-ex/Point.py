import math

class Point(object):
    """Represents 2D points"""


p = Point()
p.x = 3.0
p.y = 4.0

def print_point(pt):
    print '(%s,%s)' % (pt.x,pt.y)


print_point(p)

def point_dist(p1,p2):
    return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)


p2 = Point()
p2.x = 7.0
p2.y = 5.0

print point_dist(p,p2)
