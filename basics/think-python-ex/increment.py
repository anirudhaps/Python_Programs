'''
Exercise 16-3
'''
class Time(object):
    '''
    
    '''


def increment(t,sec):
    t.seconds+=sec
    if t.seconds>=60:
        q,r = divmod(t.seconds,60)
        t.minutes+=q
        t.seconds = r
    
    if t.minutes>=60:
        q,r = divmod(t.minutes,60)
        t.hours+=q
        t.minutes = r
    
    if t.hours>=24:
        q,r = divmod(t.hours,24)
        t.hours = r
