# how to print a value, present in a dictionary, using 'print %s' statement

def profile(**cred):
    print 'I studied %(subject)s in class %(standard)s' % cred

profile(subject='physics',standard='11th')
profile(standard='8th',subject='Social Science')
d = {'subject':'Environment','standard':'5th'}
profile(**d)
del d['subject']
print d
profile(subject='English',**d)
