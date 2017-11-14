"""
#iteration:the process of exicuting set of statements for multiple times is known as iteration or loop 
python supports 2 types of looping mechanisms they are for and while 
for loop:
	in python for is powerful and flexible iteration mechanism which doen't req variable instalisation , condition pattern and increment decrement 
	in python for loop will work along with membership operator 'in' which will work as assingment operater
	for loop will take 1 element at atime from group of elements and process if the operation of block statement 
	this process will repeat for n no of times here n nothing but no of elements in group
syntax:
    for variable in group of elements

data=[1,2,3,5,6]
for i in data:
	print i

data=[1,2,3,5,6] # for even numbers
for i in data:
	if i%2==0:
		print i
"""
data=[1,2,3,5,6] #for odd numbers
for i in data:
	if i%2!=0:
		print i

data=[1,2,3,5,6]  #its saving op in a list
data1=[]
for i in data:
	if i%2==0:
		data1.append(i)
print data1	
"""
control statement: python supports 2 types of control statements(key words)
they are break and continue
break: this key word is used to exit from complet iteration process
continue: this key word is used to skip the current iteration and continue with next iteration

"""
l=[1,2,3]
for i in l:
	if i%2==0:
		print "{0} is even number".format(i)
		break
	else:
		print "{0} not even number".format(i)	

h=[1,2,3,4,5,6]
for i in h:
	if i%2==0:
		print "{0} is even number".format(i)
		continue 
		print "i am even"
	else:
		print "{0} is odd number".format(i)	

"""
swaping:
a,b=10,20
a,b=b,a
print a,b	"""	

"""
while loop:
	while ioop requires the variable instalisation,condition and increment r decrement operation 
	the while statement will exicuies only when the condition is satiefies 
	the iteration will continues untill the condition fails
note:while loop results and infinite loop because of codeing issue 
	syntax: while(condition):
	             .................
	        "	i++
	        	"""	
i=0
while (i<10):
  print i
  i+=10

