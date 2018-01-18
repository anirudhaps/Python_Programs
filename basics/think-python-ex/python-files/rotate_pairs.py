'''
Exercise 11-10
'''

def is_rotate_pairs(a,b):
    # a and b are strings
    la = list(a)
    lb = list(b)
    if len(la)!=len(lb):
        return False
    base_diff = ord(la[0]) - ord(lb[0])
    i=1
    while i<len(la):
        diff = ord(la[i]) - ord(lb[i])
        if diff!=base_diff:
            return False
        i+=1
    return True

def rotate_pairs(lst):
    output = []
    for s in lst:
        out_lst = []
        i=lst.index(s)+1
        while i<len(lst):
            if is_rotate_pairs(s,lst[i]):
                if s not in out_lst:
                    out_lst.append(s)
                out_lst.append(lst[i])
            i+=1
        output.append(out_lst)
    return output
