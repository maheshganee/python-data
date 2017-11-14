#LIST:the group of element enclosed bt 2 square brakets is known as a list in python
"""in list elements should separated by ,s elements can be of any type
list is ordered data strucutre
list is mutable data structure so hence we can perform CRUD operation 
syntax: list_name=[ele0,ele1,ele2,..........]

Updating a list: to update a list in python follow the below syntax
list_name[index_position]=value
l[2]=25
print l
deleting an element from list:
deleting a list in python follow the below syntax
del l[2]
print l 

"""
l=['h','hello',2.0,[4,5,6]]
print l[2]
print l[3][0]
l[2]=25  #l[2]is here position of element its just updating the 2 value
l[0]=5   #and also update multiple opertions
print l
del l[2]
print l  # this operation only for deleting the element
print dir(l)
"""
list of function:
append:
 this method is used to add 1 element at end of the list 
this method takes exactly 1 parameter that is element and element can be of anytype 
op format is always None
syntax" list_name.append(element)
k=[1,2,3,4]
0......................................................................k.append ('mahesh')
print k

extend:
this method is used to add multiple elements(group of elements) at the end of list 
this method takes exactly 1 parameter that is data structure
op is always None
syntax:list _name.extend(data_structure)

"""
k=[1,2,3,4]
k.append ('mahesh')
print k
k.append ([5,6])
print k
k.extend('hello')
print k
k.extend([8,7])
k.insert(2,['hi'])
print k