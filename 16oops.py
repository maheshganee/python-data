"""
oops:
the senario or mechanism used to create a structure which contains group of python objects (entity) 
 is known as object oreanted pro structure
by using oops advance below 

security
enhancement 
multi_functional
re_usable

oops concepts built based on 2 major sub properties they are class and instance
class:
	class is an intity  which contains group objects
	a class can be created by using class keyword
syntax:class classname:
	...........
	..........
	.........
ex:	
 ex : 
 class A:
	x=10
	y=20

instance:
	instance is reference of the class which is used to access the class properties 
syantax:instance_name=classname()

ex:
obj = A()
print obj.x
print obj.y + obj.x
print A()
obj.z = 30 
print obj.z


note: every class function should contain self as a 1 para beacuse while calling 
	the function with the help of instants python will send the copy if instant as a 1 para meter
now self is equivqlent to instant of the class which is used to axis class propertiy from a function

note:when ever an instant created for a perticular class python will creates a new memory locations 
.....first specific instants	

constructor:
constructor is a function which will invoke automatically when a instant created for the class 
in python __init__ will works like constructor

def __init__(self):
		print "i am a constructor"
constructor do not return any thing 
__init__() should return None

note:

the main perpose of init method is used to defind pre requir data
init method will not create a new instant rather it will init 
a constructor internally calls __new__ method which is used for creation of new instant 


method overloading:

the process of creating 2 r more functions with same function name and with diff signature is known as method overloading
but technically python does not support method overloading rather we can achive this by using default para mechanism


ex:
def add (a,b,c):
	return a+b+c
def add (a,b,c,d):
	return a+b+c+d


print add(10,20,30,40)	

def add (a,b=0,*c):
	return a+b+sum(c)
print add(10,20,30,25,66) 

method overriding:

the process of creating 2 r more functions with same function name and same signature its called method overriding 
python does not support method overriding also but it can be achive by placing the functions in 2 diff class

polymorphism:
poly stands for many and morph stands for face 
the process of creating an object which will work for multiple functionalities is known as polymorphism

ex:
class A:
	def add (self,a,b,c):
		return a+b+c
class B:
	def add (self,a,b,c):
		return a-b-c

obj = A()
print obj.add(10,20,30)
obj1 =B()
print obj1.add(10,20,30


abstraction:
the process of hiding the data is known as abstraction
in python we can achive or created abstraction object by preceding __ infront of the property name
the abstarceted property over readding  by(bound with) the class name
abstarceted properties can not accessed directly rather use below syntax to access 
syntax: instantname._classname__property


encapsulation:
the process of binding the data is known as encapsulation 
in python abstraction and encapsulation can achived in the same way

ex:class A:
	__x=10
	y=20
	def add(self,a,b):
		return a+b

obj = A()
print obj._A__x
print obj.y


ex:
class A:
	__x=10
	y=20
	def __add(self):
		return self._A__x + self.y

obj = A()
print obj._A__x
print obj.y
print obj._A__add()

inheritance:
the process of aquairing the property from 1 class to another class is known as inheritance
in the inheritance the class from which we r accessing the properties is known as base r parent class 
the class in which we r accessing base class properties is known as derived r child class
python supports 3 types of inheritance they are 1 single
												2 multiple
												3 multy level
single inheritance:

the inheritance which involves 1 base and 1 derived class is known as single inheritance







multiple inheritance:

the inheritance which contains multiple base class and 1 derived class is known s multiple inheritance







multi level inheritance:

the inheritance which contains multiple base and derived classes is known as multy level inheritance







MRO:

method resolution order , which specifies the order of exicuting the properties when they are inheritated
according to MRO python will always look for the property in the class for which the instance created 
if the property is not avalable python will look inti inheritated classes in the direction of left to right 

ex:class A:
	name= 'mahesh'
	age = 25
	mobile = 9642884899
	def add(self,a,b):
		return a+b
class B():
	y=20
class C(B, A):
	z=55	

obj = C()
print obj.name


super:
super method is used to change method resolution order 
super method will apply only on new style classes (the class which inheritance )is known as new style
super method takes exactly 2 parameters they are class name and self key word
the class name should be the name of the class in which it is avalable 
super method returns an instance of inheritated class 
for this instance we can use any sublevel functionality

syntax:
super(classname,self).





ex:
class A(object):
	x = 90
	def add(self,a,b):
		return a+b
class B(A):
	def add(self,a,b):
		print super(B,self).add(a, b)
		return a * b
obj = B()
print obj.add(10,20)												
		
class method:
the methods which csan be invoke by using class name are known as class methods
class methods should decorated by @classmethod decorater 
class method should contain cls as a 1 para
these methods can be invoke either using class name r class instance 

static method:
the methods which besides in a class but they are not belongs to class are known as static method
static method should decorated by @staticmethod decorater 
there is no default 1 para for staticmethod 
these methods can be invoke either by using class name r class instance 	





ex:
class A:
	def add(self,a,b):
		return a+b
	@classmethod
	def mul(cls,a,b):
		return a*b
	@staticmethod
	def power(a,b):
		return a**b


obj = A()
print obj.add(10,20)
print A.mul(10,20)
print A.power(2,5)	
print obj.mul(5,9)
print obj.power(5,6)



"""


"""
rendering function:
rendering functions are used to transfer or send the data from views to front-end 
python supports 4 types of rendering functions they are 
HttpResponse
HttpResponseRedirect
render
render_to_response

HttpResponse:
this method is used to load text or string into the browser 
this method takes exactly 1 para that is display string 
all the rendering functions wwill work along with return statement 

syntax: def function_name(request, parameters):
			.................
			..................
			return HttpResponse('display string')

HttpResponseRedirect:
this method is used to redirect the user from view function to another url
this method takes exactly 1 para that is url to redirect 
this method also works along with return statement 

syntax:def function_name(request, parameters):
			.................
			..................
			return HttpResponseRedirect('URL')

render:
this method is used to load static html page in the browser 
this method takes exactly 2 para they are request, html page name (as a string)
syntax:def function_name(request, parameters):
			.................
			..................
			return render('request,'HTML page name')

render_to_response:

this method is used to load a dynamic html page along with the data in the format of dictionary 
this method takes 2 para they are html page name and dictionary which contain data
syntax:def function_name(request, parameters):
			.................
			..................
			return render_to_response('HTML page',{'var:val',.......})



request:
request is key word which can hold the data coming from front end 
in technical praspective request is referd as a wsgi object which contains html form data, secession data and login user informaton
to access the form data we can use the below syntax

request.methodtype

here method type rep by html methods like POST,GET,PUT and DELETE
Note:
request.methodtype is known as dictionary which contain form data

request.post
request.post['name'] or request.POST.GET('name')						







"""


