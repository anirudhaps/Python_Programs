#docstring

def cubes(x):
    '''This function prints Hello.
    This is another one.'''  #docstring    
    print 'Hello'
    'This function returns the cube of the passed argument' # not a docstring
    # The string put at the beginning of the function is stored as part of
    # this function.
    # It is called docstring.    
    return x*x*x


print cubes(10)
print cubes.__doc__   # Syntax to access the docstring of a function

# A docstring is like a comment inside a function but with a difference that
# it is stored as part of the function and can be accessed using above syntax

# If you want a string to become docstring of a function, it has to be put as
# the very first thing inside the function before any other code
# ''' is used to write multiple line string
