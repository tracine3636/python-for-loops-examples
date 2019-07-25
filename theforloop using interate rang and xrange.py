Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> // Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

// Prints out 3,4,5
for x in range(3, 6):
    print(x)

// Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
SyntaxError: invalid syntax
>>> 
>>> 
SyntaxError: //invalid syntaxFor loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, which acts like xrange). Note that the range function is zero based.
SyntaxError: invalid syntax
>>> 
>>> 
