
'''
functional programming tools------f p t are used of reduce the complexity of using for loops
//python provides four types of functional programming tools which are used to perform speicific operations they are
filter
map
reduce 
zip


filter-----this method is used to perform filtering operations on given data structures
//filter method takes exactily two prametrs first parameter function name and second parameter is data structure
//this function should defined before using filter method


note====filter method takes one element from group of elements and it will invoke (call) main parameter with one parameter 
//on succesful conditional status the function return some data and this data will be appended to the list created by filter method
// o/p format is always the type of given data structure 

def function_name(parameter)

filter (function_name,g.e)

map--------------this method is uesd to perform manupulation operation on each and every elemnt of data structure
//this method will also take exactly two parameter they are function name and group of elements
//the o/p formats alway a list

map(function_name,g.e)

reduce--------reduce method used to perform manupulation operation on all the elements
//this method will also takes two parameter like filter and map methods
//but reduce takes two elements from given data structure at a time and pass the same to the called function
//o/p is always a single element that belongs to any type

reduce(function_name,g.e)

zip---------this method will return a list of tuples as o/p which is creted from two data structure
//this method take two parameter that is d.s1 and d.s2
//o/p is always is list of tuples

to convert list of tuples into dictionary use inbuild method dict

zip(d.s1,d.s2)


'''