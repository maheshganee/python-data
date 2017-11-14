"""

Iterator: 

Iterator is container which holds group of elements that will be store in an object format
itertors can be created by using iter function

iter:this method takes exactly one parameter that is data structure
iterarors does not support iteration control behaviour(the process of controling given iterable data)
Note: python Iterator come with inbuilt function called next which is used to access the data from an iterators
next method does not req any parameter and they will popup one element from iterators
next method causes stop iteration error so its prefore to avoid next method in python 

syntax:iterator_name=iter(parameter)

l=iter([1,2,3,4])
print l 


Generators:

Generators are also used to store the data in the format of an object named as generator object
in python every generator is an iterator but not vise versa 
generator are used to control iteration behaviour 
we need to use the combination of a function along with yield keyword to create a generator 

yield statement is equivalent return key word but when ever yield key word occour for the 1 time python will 
create a generator object and for the next time it will dum the given data into generator

like Iterator in generator also we can access the data by using next method

syntax:
def generator_name(parameters):
	------------statement1
	------------statement2
	yield data

ex:def myfun(l):
	yield[ele for ele in l if ele%2==0]
x=myfun(range(10))
print x.next()	

Decorators:	

decorators are wrapper function in python which will over readden on top of main function
if we are invoking the main function python will exicute decorators function, based on the statics of decorators exicute the main function
to use a decorators function mentioned or declaried @ decorator_function_name on top of main function

syntax:@decorator_function_name
		def mainfunction (parameter)

ex:classmethod


****
note:decorators function will take exactly 1 parameter that is main function name		

Creation of decorators:



syntax:







def check_b(f):
	print "I am in Decorator"
	def wrapper(a,b):
		print "I am in wrapper"
		if b!=0:
			print "Calling Main Fun"
			return f(a,b)
		else:
			print "Returning error"
			return "b should not 0"
	print "Calling wrapper......"
	return wrapper

@check_b
def div(a,b):
	print "return a/b to wrapper"
	return a/b

print div(10,2)	

"""

def check_b(f):
	print "I am in Decorator"
	def wrapper(a,b):
		print "I am in wrapper"
		if b!=0:
			print "Calling Main Fun"
			return f(a,b)
		else:
			print "Returning error"
			return "b should not 0"
	print "Calling wrapper......"
	return wrapper

@check_b
def div(a,b):
	print "return a/b to wrapper"
	return a/b

print div(10,2)	