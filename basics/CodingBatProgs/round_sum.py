'''
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) -> 60
round_sum(12, 13, 14) -> 30
round_sum(6, 4, 4) -> 10
'''

from sys import argv

def round_sum(a,b,c):
    a = round10(a)
    b = round10(b)
    c = round10(c)
    #print a,b,c
    return a+b+c
    
def round10(num):
    rmd = num%10
    if rmd>=5:
        num = num - rmd
        num+=10
    else:
        num = num - rmd
    return num


va = int(argv[1])
vb = int(argv[2])
vc = int(argv[3])
print round_sum(va,vb,vc)
