Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> chr
<built-in function chr>
>>> help(chr)
Help on built-in function chr in module __builtin__:

chr(...)
    chr(i) -> character
    
    Return a string of one character with ordinal i; 0 <= i < 256.

>>> chr(65)
'A'
>>> nums = [65,66,67,68,69,70,71,72,73,74,75]
>>> nums
[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
>>> map(chr,nums)
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
>>> help(ord)
Help on built-in function ord in module __builtin__:

ord(...)
    ord(c) -> integer
    
    Return the integer ordinal of a one-character string.

>>> ord('c')
99
>>> map(ord,list('apsingh'))
[97, 112, 115, 105, 110, 103, 104]
>>> # Note: The map function “maps” one sequence into another (of the same length) by applying a function to each of the elements.
>>> 
>>> 
>>> map(lambda n: 2*n,nums)
[130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150]
>>> nums
[65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
>>> filter(lambda n: n%2==0,nums)
[66, 68, 70, 72, 74]
>>> filter(lambda n: n%2!=0,nums)
[65, 67, 69, 71, 73, 75]
>>> filter(max,nums)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    filter(max,nums)
TypeError: 'int' object is not iterable
>>> # The filter function returns a new list in which the elements that you don’t want have been filtered out. Or, to put it another way, it returns exactly those you do want. You supply filter with a function that returns a Boolean (truth) value for a given sequence element. If the function returns true, the element is part of the returned sequence; if it returns false, the element is not included in the returned sequence. (The original sequence is not modified.)
>>> # the first argument of filter() must be a function that tests its argument and returns true or false
>>> # the first argument of map() must be a function that maps its argument to some value
>>> reduce(max,nums)
75
>>> reduce(min,nums)
65
>>> reduce(sum,nums)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    reduce(sum,nums)
TypeError: 'int' object is not iterable
>>> reduce(lambda x,y: x+y,nums)
770
>>> # the first argument of the reduce() must be a function that takes two or more of the elements of 2nd argument(list) and returns a number
>>> def sumDev(x,y):
	print 'sum and remainder of %d %d' % (x,y)
	return (x+y)%y

>>> reduce(sumDev,nums)
sum and remainder of 65 66
sum and remainder of 65 67
sum and remainder of 65 68
sum and remainder of 65 69
sum and remainder of 65 70
sum and remainder of 65 71
sum and remainder of 65 72
sum and remainder of 65 73
sum and remainder of 65 74
sum and remainder of 65 75
65
>>> 
