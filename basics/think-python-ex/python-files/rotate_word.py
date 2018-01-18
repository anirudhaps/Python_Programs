'''
Exercise: 8-12
'''

def rotate_word(s,i):
    out_str = ''
    for c in s:
        ov = ord(c)
        ov+=int(i)
        if c.isdigit():
            if ov>ord('9'):
                r = ov % ord('9')
                fv = (ord('0')-1) + r
            elif ov<ord('0'):
                r = ord('0') - ov
                fv = (ord('9')+1) - r
            else:
                fv = ov    
        elif c.islower():
            if ov>ord('z'):
                r = ov % ord('z')
                fv = (ord('a')-1) + r
            elif ov<ord('a'):
                r = ord('a') - ov
                fv = (ord('z')+1) - r
            else:
                fv = ov
        elif c.isupper():
            if ov>ord('Z'):
                r = ov % ord('Z')
                fv = (ord('A')-1) + r
            elif ov<ord('A'):
                r = ord('A') - ov
                fv = (ord('Z')+1) - r
            else:
                fv = ov        
        out_str = out_str + chr(fv)
    return out_str
    
string = raw_input('Enter any string: ')
index = raw_input('increment: ')
print 'Encrypted string:', rotate_word(string,index)
