from swampy.TurtleWorld import *

world = TurtleWorld()
#print world
bob = Turtle()
print bob
#fd(bob,100)
#lt(bob)
#fd(bob,100)
#lt(bob)
#fd(bob,100)
#lt(bob)
#fd(bob,100)
for i in range(4):
    fd(bob,100)
    lt(bob)
wait_for_user()

#imp: installation of a package in python: download the package, unzip it, go into the package directory and then:
# type: 'sudo python setup.py install' on terminal if the folder contains setup.py file otherwise write the name of the 
# setup file present in the folder

# To install package in python: $ sudo pip install <package-name> 
