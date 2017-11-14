"""shallow copy: 
the process of copying the memory location from 1 variable to another variable is known as shallow copy
rules of shallow copy:
2 r more variables must share a single memory location 
if 1 variable data gets change another data will get change automatically

syntax:
variable 2 = variable 1
 
shallow copy on mutable objects:
as we can change the data of mutable data structures they will obey the rules of shallow copy perfectly
ex:a=[1,2,3]
   b=a
   print id(a)
   print id(b)
a[1] = 10
print a
print b 

shallow copy on immutable objects:
as we can't modify the data in immutable data structures they will not obey the properties of shallow copy completely

ex:s='hello'
v=s
print v
print id(v)
print id(s)
s = 'python'
print id(s)
print v

deep copy:the process of copying the data from 1 variable to another variable is known as deep copy 
in deep copy 2 r more variables will share the same data with diff memory location 
Note:in orderd data structures we can perform deep copy by using slicing process and to acheive deep copy unorderd data structures we will copy
ex:a=[1,2,3]
b=a[::]
print b
print id(a),id(b)

"""