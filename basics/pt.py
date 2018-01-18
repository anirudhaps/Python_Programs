Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 7/-3
-3
>>> a = 2+1j
>>> a
(2+1j)
>>> a.real
2.0
>>> a.imag
1.0
>>> b = 2 + j

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b = 2 + j
NameError: name 'j' is not defined
>>> b = complex(2,1)
>>> b
(2+1j)
>>> a + b
(4+2j)
>>> b = complex(4,3)
>>> b
(4+3j)
>>> a+b
(6+4j)
>>> a
(2+1j)
>>> b
(4+3j)
>>> a * b
(5+10j)
>>> a / b
(0.44-0.08j)
>>> a
(2+1j)
>>> abs(a)
2.23606797749979
>>> b
(4+3j)
>>> abs(b)
5.0
>>> c = 2.345678
>>> round(c,2)
2.35
>>> help(round)
Help on built-in function round in module __builtin__:

round(...)
    round(number[, ndigits]) -> floating point number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative.

>>> round(c)
2.0
>>> round(2,1)
2.0
>>> round(2,2)
2.0
>>> round(c,1)
2.3
>>> round(c,2)
2.35
>>> round(c,3)
2.346
>>> round(c,4)
2.3457
>>> round(c,5)
2.34568
>>> round(c,6)
2.345678
>>> _
2.345678
>>> _ = 5
>>> _
5
>>> a
(2+1j)
>>> _
5
>>> name = "my name is anirudha.\n\"
SyntaxError: EOL while scanning string literal
>>> name

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = "my name is anirudha.\
I am studying in Mtech IT at UOH, hyderabad.\n\
My aim is to get a software job."
>>> name
'my name is anirudha.I am studying in Mtech IT at UOH, hyderabad.\nMy aim is to get a software job.'
>>> print name
my name is anirudha.I am studying in Mtech IT at UOH, hyderabad.
My aim is to get a software job.
>>> hello = '''
Hi, I am anirudha.
I would like to say hello to everyone.
Nice to meet you all.
'''
>>> hello
'\nHi, I am anirudha.\nI would like to say hello to everyone.\nNice to meet you all.\n'
>>> print hello

Hi, I am anirudha.
I would like to say hello to everyone.
Nice to meet you all.

>>> xn = r'this is another example.\n\
kindly, see the r prepended to this string.'
>>> xn
'this is another example.\\n\\\nkindly, see the r prepended to this string.'
>>> print xn
this is another example.\n\
kindly, see the r prepended to this string.
>>> ys = "hello"
>>> ys
'hello'
>>> ys = ys + 'Hi'
>>> ys
'helloHi'
>>> ys*5
'helloHihelloHihelloHihelloHihelloHi'
>>> 'anirudha' ' pratap' ' singh'
'anirudha pratap singh'
>>> help(strip)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    help(strip)
NameError: name 'strip' is not defined
>>> dir(string)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dir(string)
NameError: name 'string' is not defined
>>> import string
>>> dir(string)
['Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_float', '_idmap', '_idmapL', '_int', '_long', '_multimap', '_re', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'atof', 'atof_error', 'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count', 'digits', 'expandtabs', 'find', 'hexdigits', 'index', 'index_error', 'join', 'joinfields', 'letters', 'ljust', 'lower', 'lowercase', 'lstrip', 'maketrans', 'octdigits', 'printable', 'punctuation', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate', 'upper', 'uppercase', 'whitespace', 'zfill']
>>> help(string.strip)
Help on function strip in module string:

strip(s, chars=None)
    strip(s [,chars]) -> string
    
    Return a copy of the string s with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping.

>>> none

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    none
NameError: name 'none' is not defined
>>> print None
None
>>> help(None)
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __hash__(...)
 |      x.__hash__() <==> hash(x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)

>>> None
>>> dic = {}
>>> dic
{}
>>> dic['a'] = 'anirudha'
>>> dic['r'] = 'rahul'
>>> dic['c'] = 'claudia'
>>> dic
{'a': 'anirudha', 'c': 'claudia', 'r': 'rahul'}
>>> dic['r']
'rahul'
>>> dic.get('r')
'rahul'
>>> dic['x']

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dic['x']
KeyError: 'x'
>>> dic.get('x')
>>> dic.keys()
['a', 'c', 'r']
>>> dic.values()
['anirudha', 'claudia', 'rahul']
>>> 'a' in dic
True
>>> 'claudia' in dic
False
>>> for n in dic.keys():
	print dic[n]

	
anirudha
claudia
rahul
>>> for n in sorted(dic.keys()):
	print dic[n]
	\

	  
SyntaxError: invalid syntax
>>> for n in sorted(dic.keys()):
	print dic[n]

	
anirudha
claudia
rahul
>>> dic.items()
[('a', 'anirudha'), ('c', 'claudia'), ('r', 'rahul')]
>>> for n in dic.items():
	print n

	
('a', 'anirudha')
('c', 'claudia')
('r', 'rahul')
>>> ================================ RESTART ================================
>>> 
Summer is started.

I am fealing hot in afternoon.

It's OK. I'll manage.

I will switch on fan.
>>> ================================ RESTART ================================
>>> 
Summer is started.
I am fealing hot in afternoon.
It's OK. I'll manage.
I will switch on fan.
>>> 
