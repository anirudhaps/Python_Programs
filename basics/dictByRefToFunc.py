# passing the dictionary to a function by reference

def init(d):
    d['first'] = {}
    d['middle'] = {}
    d['last'] = {}


storage = {}
print 'Storage before calling init on it: ', storage
init(storage)
print 'Storage after calling init on it: ', storage

# after calling init, the storage and d both refer to same dictionary


# Note: The keys of a dictionary don’t have a specific order, so when a
# dictionary is printed out, the order may vary. If the order is different in
# your interpreter, don’t worry about it.
