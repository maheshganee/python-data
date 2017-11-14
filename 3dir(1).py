
#DIR: 
s="python"
print dir(s)
"""
this method will return list of directive or prop of given variable
this method takes exactly one parameter that is variable name
op format is always a list 
syntax:dir(variable\data)
note:to access sublevel functionality of a variable use .(dot)
Ex:variable_name.function

string function:
1 upper:this method will return the copy of upper case converter string 
no parametrs required 
op format is always string
ex:print data.upper()
2 lower : this method will return the copy of lower case converter string
no parameter required 
op format is always string
ex:print data.lower()
note:python supports 2 types of data units they are mutable and immutable data unit 
     the data unit which can modified is known as mutable data unit
     the data unit which can't modified is known as immutable data unit 
     strings are immutable data structure


"""
data = "mahesh"
print data.upper()
print data.lower()
print data.count('h')
print data.capitalize()
print data.isalpha()
s_en = data.encode('base64')

"""
3.count: the method will return the count of (the no of occurances of ) given substring
this method will takes exactly one parameter that is substring
print data.count('h')
op format is always is integer
4.capitalize:
print data.capitalize()#no parameter required
this method will return the copy of capitalize string (1 letter will convert in to caps)
op is a string
string_name.caps()
ex: print data.capitalize()
5.isalpha:
it contain only alphabits
its op always boolen 
ex: print data.isalpha()
6.isdigit:
ex: print data.isdigit()
7.isalnum:
ex: print data.isalnum()
"""
data = 'python'
print data.encode("base64")
print s_en.decode('base64')
print data.endswith('sh')
print data.startswith('mah')
print data.index('h')
print data.find('t')
print data.find('k')
x = 'hello python world'
print x.split('o')
print '@'.join(x.split('o'))

"""
8. encode : this method will return the copy of encrypted string
this method will take exactly1 parameter that is enscription format
op format is always string
syntax:print data.encode("base64")
9. decode:
this method will return the copy of descrypted string
op format is always string
print s_en.decode('base64')
10.starswith: this method will return to only if the string started with given substring
this method takes exactly1 1 parameter that is sub string
op format is always boolean operator
 this method will check the starting 
   syn: print data.startswith('mah')
11. endswith: his method will return to only if the string started with given substring
this method takes exactly1 1 parameter that is sub string
op format is always boolean operator
this method checks the ending 
    syn: print data.endswith('sh')
12. index: this method will return the index position of given substring
this method takes atleast 1 parameter at most 2 parameters
1 parameter rep the substring and 2 parameter rep index position from where to search for given substring 

 syn: string_name.index('substring')
for one more print data.index('w',data.index('w')+1) (or)  string_name.index('substring',index position )
if letter not in the sub string it will show error
13. find: this method will also work like index method but find method will return -1 if substring not found instead of error
print data.find('t')
14.split: this method is used to split the given string into multiple parts based on given substring
x = 'hello python world'
this method takes atmost 1 parameter that is substring if no parameter given python will consider it as space and op format is aiways list
print x.split('o')

15.join:
this method will return joined string of given list 
the list will get joined by using given substring 
this method takes exactly 1 parameter that is list 
'substring'.join(list)
17.strip:
this method is used to remove the subsrting from given string 
the process of removing the edges will be done at both the sides (left and reght)
this method takes atmost 1 parameter that is substring and the default value is space( )
syntax: string_name.strip('substring')
ex:print l.strip('h')
18. lstrip: this method will return the copy of given string in which the substring removed from left hand side only 
19. rstrip: this method will return the copy of given string in which the substring removed from right hand side only
print l.lstrip('h')
20. format: this method will return the copy of given dynamic string in which variables were replaced with given values
the no of perameters passing to this method = no of variables 
op format is always string
syntax: s="hello {name}"     (variable format method)
string_name.format(v1=val1,v2=val2........)
print s.format(name='mahesh')
using index position
s="dear {0},your ticket from {1} to {2} has neeb booked"
print s.format('mahesh','badvel','bang')
21.replace:this method will return the copy of replaced string 
this method takes 2 parameters they are substring to replace and substring to place 
syntax: s.replace('string to replace','string to place')
print s.replace('o','@')
22.isupper: this method will return through only if the given string contains all the upper case char
no parameter req
op format is always boolen 
      print s.isupper()
23.islower:this method will return through only if the given string contains all the lower case char
no parameter req
op format is always boolen 
syntax:  string_name.islower()
        print s.islower()      
"""
y = '''mahesh 
welcome to banagalore'''
print y.split('\n')
l = 'hello'
print l.strip('h')
g = "hello {name}"
print g.format(name='mahesh')


"""append
extend
insert
pop
remove
index
sort
re"""
