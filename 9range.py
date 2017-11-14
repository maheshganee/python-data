"""
Range:
this method will return a list of sequence numbers based on given set of parameters
range method takes atleast 1 parameter atmost 3 parameter
1 parameter rep the starting element req op and the default value for p1 is 0
2 parameter rep ending element in req op and it is madetatory parameter 
3 parameter rep no of altenative element and default value of p3 is 1

ex:a=range(8,25)
print a

xrange:
this method will also works like range method but it will return an xrange object as op,which takes less memory to take and less time to exicute
Note:in python 2.x both range and xrange method avalable but 3.x only range avalable (xrange properties were mapped to range and x range method deprecated)

a=xrange(-1,-10,-1)
for i in a:
	print i

type conversion:
int to float=












funnctions:
the set of statements which are used to perform specific task is known as function 
these are devided into 2 types they are 1 calling 2.called function
1.called:the function which created with the help of def key word, it contains function name set of parameters, set of statements along with return key word is konwn as called function
 a called function  exicutes only when we have created a calling function

 syntax:def function_name(parameters):
 	.................
 	.............
 	return(parameters)



EX:def add(a,b):
	return(a+b)

print add(10,15)


2.calling : it is an initiative of called function which contains function name along with set of parameters only

syntax: function_name(parameters)

NOTE:the data can be traversed(transfer) from called to calling with the help of return key word
the main perpose of function is reusability and we can exicute a specific peace of code insted of complete file

default function:
default parameters are used to extend the function accessbility by placing parameters assignment in called function signature
the default parameters should always fallowed by mandetary parameter
if no values passed to default parameter python will assign the value given in function signature
Note:function variable life time is always with in a function 
i.e function variable are private to the function 

def add(a,b=0,c=0):
	return a+b+c
print add(1)


*args: 
this parameter is used to accept unknown no.of parameters
these parameters will be save in format of tuple 
note:use * variable name only in function signature 


ex:def add(*c):
	print c
	return sum(c)
print add(1,2,3,55,58,99,4)

ex:def add(a,b=0,*c):
	print a
	print b
	print c
	return a+b+sum(c)
print add(1,2,3,55,58,99,4)

**kwargs:
this variable is used to accept unknown no.of items in the format of dictionary 
these items should pass in the form of variable assignment 


syntax:function(k1=variable,k2=variable,k3=variable....)


ex:def add(**c):
	print c
	return sum(c.values())
print add(a=1,b=20)		

def add(a,b=0,c=0,*d,**e):
	print a
	print b
	print c
	print d
	print e
	return a+b+c+sum(d)+sum(e.values())
print add(10,2,3,4,5,6,78,9,x=1,y=20)





"""


