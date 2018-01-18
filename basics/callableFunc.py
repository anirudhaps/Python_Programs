#a demo for collable() function

import math

x = 1
y = math.sqrt

if callable(y)==True:
    print y(36)

print 'Output values for callable() function:'
print callable(x)
print callable(y)

# callable(argf) returns True iff argf is a function that can be called
# Otherwise, it returns False
