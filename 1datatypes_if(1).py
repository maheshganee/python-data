'''
data types:	
            1.integer
            2.float
 Integer:The medium which allows the prohramming language to deside what kind data to be store known as data type 
           python supports two types of d
 integer:The medium or data type which can hole only numarical values is known as integer
 syntax :variable name =numarical value                    
Float:The medium which can hole numaric data along with decimal is known as float data type
ex:'''
salary=2686.85
print type(salary)
"""
inbuilt function: 
function: The set of statements which off used to perform particular task is known as a function in python 
,every function should contain paranathsys and limit numb off parameters /arguments/signatures
inbuilt function;The function which comes with default python function are known as inbuilt function 
Type:This method will return the type off given variable 
     This method takes exactly one parameter that is varabile name 
     The output format is always type off varable 
Syntax:type (variable)
ex:type(a)=type('int')"""
a=10.08
print type(a)
# op: type('float')

"""
This method is used to display the given in output window 
This method can takes any numb of parameter 
Note:in two point x version python can be operator either or key word or function 
     but in3.x version print can use only a function 
syntax:print(data to put in output)
ex:"""
a,b = 10,20
"""
Multi variable assignment: a,b=10,20
note:why working with multi variable assignement python will create a touple arround the operator and then compare both the data 
     on succ comparison python will       variable assignment 
inbuilt menthod:"""
      
'''id:-this method will the memory will location given variable 
       This method takes exactly one parameter that is variable name 
       output format is always memory location numb
syntax:-print id(variable name)'''

a=10
b=20
print id(a)
print id(b)
'''types of memory unit:-1.stack
                         2.quaue
                         3.heap
 -python supports two types memory units they are order memory units and un oeder memory unit 
 order memory units:-the memory units which can stores the data in order format are known as order memory units 
 ex:-stack and quaue 
 _un oredr mery units:-the memory units which can store the data in randam format are kown as un order memory units
 ex:-heap                          