'''
Exercise: 11-9
'''

def has_duplicates_v2(lst):
    d = dict()
    for i in lst:
        if i in d:
            return True
        else:
            d[i] = 1
    return False
