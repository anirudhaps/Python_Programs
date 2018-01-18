#infinite loops and breaking out of them

print 'Creating a list of numbers>=0:'
lst = []
print 'Keep entering numbers. When you want to stop, enter any number<0.'
while 1:    #infinite loop because condition will always be true
    item = input('Enter any number: ')
    if item<0:
        break
    else:
        lst.append(item)
print lst
    
     
    
