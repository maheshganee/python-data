"""
strings
the groupof char whick are enclose btw '' r '' '' r ''' ''' are known as strings in python 
-single code strings r '' are used to create online string, but ''' strings use to create multi line strings 
-note:when we press enter bt the quatation python will consider (new line ) and \ n also one char
- any thing comes bt quatation is known as a string 
-strings are orderd data structure:-
the data structure from which we can acess the data by using indexing process are known as ODS
in python indexing is devided into 2 types they are 1.possitive indexing 2.negitive indexing
possitive indexing:indexing the direction of left to right is known as PI
in possitive indexing the left most element is always 0 and it will increment by 1 for each right most element 
the last element position length of elements -1
negative indexing: the indexing in the direction of right to left is kniwn as negative 
in negative the right most element indexing will always start with -1 and it will decrement by 1 for every 
the last element index position is always (-)length of the string  
use sqare brakets while working in sliceing

"""

s= 'python'
print id(s)
print s[5]
''' 
IndexError: string index out of range because of 7 is not in the string its start from 0 to 5
0 to 5 is called index number 
'''
s='python'
print s [1:5:1]
print s [5:2:-1]
print s [4:1:-2]
print s [1:5:2]
print s[::]
'''
from the above syntax s[p1:p2:p3]
here p1 is start of required 
SLICING: the process of taking required data from group of elements is known as SLICING
in python slicing is devided into 2 types they are positive slicing and negative slicing 
slicing to perform slicing use [] which will opt max 3 parameters which are separated by using ::
string_name[p1:p2:p3]
3rd parameter rep no of alternate elements in the form of integers
the default of p3 value is always +1

positive slicing:slicing in the direction of left to right is known as +slicing
in +slicing p1 rep starting  starting element in required data the default value is 0
p2 2nd parameter rep ending element index position of req data the default value length of data structure
p3 3rd rep the direction of string
-slicing: in the direction of right to left 
p1 default value -1
p2 default (-length(data structure)-1)
**** reversing the string s[::-1]

welcome"
"WeU"
"nohtyp"
"nt  oe"

'''
#task: variable name data
data = 'hi user, welcome to python world'
print data[10:17]
print data[27:21]
'''
length:this method will writen no of element in given data structure
this method will take exactly 1 parameter data structure
op format is integer
INPUT: this method is used to get the data from the user 
this method takes exactly 1 parameter that is display string it will not return so op is None
RAW_input:'''
age=raw_inpit("enter the age")
'''this method is also used t get the data from the user but python will convert the give data in string format saves into the variable
this method will take exactly 1 parameter data structure
op format is integer
INPUT: this method is used to get the data from the user 
this method takes exactly 1 parameter that is display string it will not return so op is None
variable_name=raw_input("display string")
age=raw_input("enter your age")
print age, type (age)