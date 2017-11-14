"""
dictionaries:
the group of items enclosed btw 2 {} are known as dictionaries in python 
an item is combination of key and values
in dictionaries keys should be immutable data objects and values can be of anytype
note:we can not use a mutable object as a key in dictionarie
dictionarie are mutable data structure and unorder data structure
syntax:
dict={item1,item2,....}
dictionaries={key1:value1,key2:value2,........}

dictionaries are very efficient and  fast when comparied with other data structures in python
to access the data from dictionaries we will use a process known as key 
"""
l={'a':1,'b':2,'c':3}
print l['b'],l['a']

d={1179: {'name':'mahesh','salary':1000,'company':'intel'}}
data=d[1179]
print d[1179]['company']

"""
updating an element:


"""
m={'a':1,'b':2,'c':3}
m['a']
m['c']=20   #updating the value
m['d']=15   #adding another element
del m['c']   #deleting the element
print m
z={'a':1,'b':2,'c':3,'a':8}
print z

"""
dictionary functions:

1.keys: this method will return list of keys from given dictionary
no parameter req 
op is list
ex:print z.keys()    #['a', 'c', 'b']
 #it will show the only keys in the dictionary and the op is list

2.values:this method will return list of values from given dictionary
no parameter req 
op is list
ex:print z.values()   #[1, 3, 2]
it will show the only values in the dictionary and the op is list

3.items:this method will return list of items from given dictionary
no parameter req 
op is list of tupples and each tupple contain key and value separated by(,)
ex:print z.items()    #[('a', 1), ('c', 3), ('b', 2)]

4.viewkeys:this method will return list of keys which are enclosed btw dict_keys method
no parameter req
op is dict_keys function

5.viewvalues:this method will return list of values which are enclosed btw dict_keys method
no parameter req
op is dict_values function

6.viewitems:this method will return list of items which are enclosed btw dict_keys method
no parameter req
op is dict_items function

7.iterkeys:this method will return list of keys from given dictionary which are enclosed btw dictionary-keyiterator object
op is iterater object
no parameter req
8.itervalues:this method will return list of values from given dictionary which are enclosed btw dictionary-valueiterator object
op is iterater object
no parameter req
9.iteritems:



10.has_keys:this method will return to only if the given key is avalable in dictionary
it will take exactly 1 parameter that is key
op is boolean operater 

ex:print z.has_key('a')

11.update:this method is used to update 1 dictionary with another 
this method takes exactly 1 parameter that is dictionary
op is None

12.clear: this method is used to swap the dictionary (to empty the dictionary)
no parameter req
op is None
ex:   d.clear()
      print d

13.get: this method is used to get the value at given key 
this method takes atleast 1 parameters and  atmost 2 parameters
1 parameter rep key and it is manditary 2 rep default value tobe return when key is nit avalable
the default for 2 parameter is always None
op is value at given key 
syntax:dictionary_name.get('key')
note : get methosd will not effect the dictionary

print z.get('a')
print z.get('g',10) # at the time 2 value exicute  

14.setdefault:this method will return the value at given key if key in avalable in given dictionary
if key is not avalable then it will return the default value and insert given key value pay into dictionary
this method takes atleast 1 parameters and  atmost 2 parameters
1 parameter rep key and it is manditary 2 rep default value tobe return when key is nit avalable
the default for 2 parameter is always None
op is value at given key 


print z.setdefault('c') #its shows the default value
print z.setdefault('f',10) #its creat new item
print z.setdefault('f')  #it shows None

15.pop: this method will return the value at given key and deete the appropiate item from dictionary
this method takes exactly 1 parameter that is key
op is value at given key

z={'a':1,'b':2,'c':3}
print z.pop('a')
print z

16.popitem:this method will return the 1st item in the dictionary and delete its 
no parameter req 
op is tupple

z={'a':1,'b':2,'c':3}
print z.popitem()
print z

17.fromkey:

"""

z={'a':1,'b':2,'c':3}
print z.keys()    #['a', 'c', 'b']
print z.values()   #[1, 3, 2]
print z.items()    #[('a', 1), ('c', 3), ('b', 2)]
print z.viewkeys()  #dict_keys(['a', 'c', 'b']) it will take less memory 
print z.viewvalues() #dict_values([1, 3, 2])
print z.viewitems()  #dict_items([('a', 1), ('c', 3), ('b', 2)])
print z.iterkeys()   #<dictionary-keyiterator object at 0xb71b78ec>
print z.itervalues()  #<dictionary-valueiterator object at 0xb72188ec>
print z.iteritems() 
print z.get('a')
print z.setdefault('c')
print z.pop('a')
print z

 #<dictionary-itemiterator object at 0xb72188ec>
#for ele in z.iterkeys():
#	print ele

#for i in 'hello':
#	print i,
print z.has_key('a')  # boolean operater is op
d.clear()
print d
s1={'a':1,'b':2}
s2={'c':3,'a':5}
s2.update(s1)
print s2

