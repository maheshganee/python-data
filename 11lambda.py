"""lambda function: its known as unominos function in python which can be created  by lambda key word
the scope of lambda are very limited because these are 1 line function 
lambda function doesn't req return statement 
lambda function accepts 2 sections which are separated by :
section1 contains set of parameters and section2 contains operation, function name should declear as a variable 

syntax: file_name=lambda parameters : operation

ex:acc=lambda a,b:a+b
print acc(10,20)

print filter(lambda a : a%2==0 , range(0,10))

m=[1,2,3,4,5]
m1=[]
for i in m:
	m1.append(str(i))
print m1

print map(str,m)
print map(lambda a:str(a),m)



list comprehension:
the process of creating a complex data list in a easy process is known as list comprehension
list comprehension should always enclosed  []
list comprehension may contains 2 r 3 r 4 sections

2 sections:
[sec1 sec2] #1 is operation #2 is looping   --->>>print [i*2 for i in range(5)]
3 sections:
[sec1 sec2 sec3] #1 operation #2 looping #3 condition
--->>>print [ele for ele in range(10) if ele%2==0]
4 sections:
--->>>print ['even' if ele%2==0 else 'odd' for ele in range(7)]


dictionary comprehension:


print {ele:l1.count(ele) for ele in l1 }
print {ele:l1.count(ele) for ele in l1 if ele<2}

"""


