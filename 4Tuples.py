"""
#Tuples:
the group of elements enclosed by 2 paranthasis are known as a tuple 
elements are separated by (,)and elements can be any type
tuples are orderd and immutable data structure
we can not modify the elements of tuples
but in special cases like inserting a mutable object we can modify the tuple
syntax:tuple_name=(e1,e2,e3.....)
"""
t=(1,2,3,[6,9])
t[3][1]=10
print t

"""
#membership operator:
the operators which r used to check the membership of an element in group of elements r known as membership operators 
python supports 2 types of membership operators they are 'in' and 'not in'
membership operators will allways writens boolean operator as op based on avalability of an element 

"""
l=(1,5,9,10)
print 5 in l
print 0 in l
print 5 not in l

"""
# identity operators:         # no need to work on it .
these operators are use to compare the memory locations of 2 operends 
python supports 2 types of identity operators they are 'is' and 'is not'
identity operators will always returns boolean operators as op

"""
a=10
b=20
print a is not b

"""
#block:   group of statements are known as block 
in python and the rules and regulation to follow while creating block are known as indentation
indentation rule: every block should starts with (:)
				  every statement in block should contain unique no of spaces( )
syntax: block_name:
            line 1
            line2
            line3
            Conditional block, loop,functional, classes, 

1.Conditional block : 
Conditional blocks are used to handle the Conditional status
python supports 3 types of Conditional blocks they are 'if','if else', elif ladder
if block is used to handle successful condition only that means when ever the condition is True then only the block statement exicute are else python will skip the block


if : this block is used to handle both successful and failure status of one condition 
in if else we should write 2 block 
if block will exicute only when the condition is success 
if the condition fails only else block will exicute

elif_ladder:elif ladder is used to handle the status of multiple condition 
this conditional block should contain 1 if, 1 else and atleast 1 elif 
among multiple block only 1 block exicute multiple time



"""
name = ('python is my world')
a='my'
if a in name:
	print "i am in main data"
else:
	print "i am out of range"

data = [1,6,8,9]
a=10
b=5
c = 7
if a in data:
	print "i am in"	
elif b in data:
	print "i am here"
elif c in data:
	print "c in data"
else:
    print "i am in out of range"	

l=10
k=20
if l<k:
	print "k is big"
else:
	print "l is big"    




