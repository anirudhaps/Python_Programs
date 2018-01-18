def nested_sum(lst):
    tot = 0
    for l in lst:
        tot+=sum(l)
    return tot
    
lst = [[1,2],[3,4,5],[6,7,8,9]]
print nested_sum(lst)
