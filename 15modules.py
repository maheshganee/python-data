"""
modules:
modules is a container which can hold any kind of python object 
that means every python file can be printed as a module in python 
python supports 3 types of modules they are 
1.user defind 
2.inbuild (systen defind)
3.third party modules


user defind modules:
the modules which defind by the user based on req are known as user defind modules 

accessing modules:
to accesss the data from 1 module python privide 2 types of methodology
1.import
2.from-import


1.import:this key word is used to import the high level herache of the sugested module/package
		 python will consume memory alocation for the all object which specified in given module even unused 

		 syntax:imoprt module_name
		 		module_name.property1
		 		module_name.property2
		 		.
		 		.
		 		.
		 		. 
		 		def add(a,b):
				return a+b

				def mul(a,b):
				return a*b

				2file
				import mahesh
				print mahesh.add(10,20)
				print mahesh.mul(3,6)

note: the namr defind after import keyword should only used while accessing the property
	  to over come the memory consumption problem which caused while using import key word python
	   provides from-import
from-import:
this statement is used to import the specific properties of perticular module 
in from-import the import statement should contain the lower herache 

note: from key word may contain multiple sub level property but import should only contain lower level property

syntax:from module_name import property

from module_name import p1,p2,p3

from module_name import *

package:it is also a container which holds group of python files as a folder 
but folder belongs to operating system 
to convert a normal folder into python package create a package initilizer file under the folder(__init__.py)

ex:def add(a,b):
	return a+b

	2 file
	from ganee.mahesh import add
	print add(10,20)

in-built modules:
the modules which comes with the default python version are known as in-built modules 
ex:os sys email datetime math re types requests collection time urlib urlib2 signal pdb socket threading json xml



third party modules:
the modules neigther avalable in python nor defind by the user are known as third party modules

ex:xlrd xlwt pytz django pandas numpy pdfkit suds beautifulsoup scrappy



"""
import datetime
print datetime.datetime.now()