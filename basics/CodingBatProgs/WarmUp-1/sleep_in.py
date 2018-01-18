'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) -> True
sleep_in(True, False) -> False
sleep_in(False, True) -> True
'''

def sleep_in(weekday,vacation):
	if weekday==True and vacation==True:
		print 'Invalid combination.'
	elif weekday==True and vacation==False:
		return False
	elif weekday==False and vacation==False:
		return True
	else:
		return True

print sleep_in(True,False)
print sleep_in(True,True)  #If we do not explicitly tell a function what to return, it returns None
print sleep_in(False,False)
print sleep_in(False,True)
