'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') -> True
xyz_there('abc.xyz') -> False
xyz_there('xyz.abc') -> True
'''

from sys import argv

def xyz_there(dstr):
    if '.xyz' in dstr:
        return False
    elif 'xyz' in dstr:
        return True
    else:
        return False


print xyz_there(argv[1])
