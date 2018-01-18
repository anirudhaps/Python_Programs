# passing key-value pair to a function

def dictionary(**d):
    print d
    for key in d:
        print key, ':', d[key]


dictionary(a=10,b=20,c=30,name='anirudha',work='intern')
