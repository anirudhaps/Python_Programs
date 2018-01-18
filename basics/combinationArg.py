# combination of normal arguments, passing arguments that become tuple inside
# the function and passing key-value pairs that together become a dictionary
# inside the function

def printVal(name, *courses, **details):
    print name + ':'
    print 'details:', details
    print 'courses taken:', courses


printVal('Anirudha','CN','OS','DS',age=25,status='single',message='this is not an invitation')

# rule: normal arguments and tuple must come before the dictionary argument

