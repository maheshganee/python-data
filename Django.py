"""
installing 3party modules:
a 3 party module can downloaded by using setup tools 
more than operating systems will comes with 4 major setup tools they are 

pip
apt-get
wget
easy_install

pip:

pip stands for package installer 
it os neighter avalable in windows nor in linux
to use pip we should pre install it 
syntax:pip install package_name==version

apt-get:

this tool will comes with all the operating system supportablity except windows
syntax: sudo apt-get install package_name

wget:
wget "URL"

easy_install:
easy_install package_name  
note:apt-get, wget and easy_install

source code installation:
follow the below process to download the 3 party modules using source code
1.dowwnload the source code from the internet (zip or tar.gz)
2.extract the source code which results a folder in specific location 
3.locate and navigate to the directry where setup.py file avalaable (through commend prompt)
4.run the below command to install the package (python setup.py install)

DJANGO:
1.django is a frame work which is used to create r develope web applications 
2.it is a 3 party module or package which built based on python 
3.django comes with multiple plugin accesebility so that we can intigrate any service with django 
4.django is light weight frame work (modularity) which supports multilevel modularity 
5.django comes with lazy loading process which helps to consume less memory 


django follows the oldest designed pattren or architechture named as MVC 
  but it is after the modification its using MVT


MVC: 
mvc stands for model view controller





Model:
model is data abstaction layer which holds the data required for data(model=database)
View:
view is a combination of bussiness logic layer and presentation layer
bussiness logic layer:the layer which contains the set of logical statements are known as bussiness logical layer
(what to do with data)
presentation layer:the layer which contains front end related files is known as presentation layer 
(how to display the data)
Note:
django follows mvc principles but it will work based on MVT architechture 

MVT:
mvt stand for model view templet 
1.model rep data abstaction layer
2.view rep the combination of b.l.l and controller
3.templet rep presentation layer

work flow: when ever an URL enter the by the user django will look into URLS.py file
URLS.py file is known as url mapping file which contains list of urls and they appropiate functions
when ever the url matches with any of urls.py file urls then django will goto views layer and exicute the apporiate functions
from the views we can make a req to the models to get the data from database and we can make a req to templet to get the front end files,this will be treated as responce 
the responce will be loaded in the browser through views 


"""

"""
Project:
a project is nothing but a folder which can hold 1 or more applications 
but an applications should enclosed by a project 
creating a django project:
to create a django project we will use django administation file which is named as django-admin.py file
run the bellow command to create a project 

--->>>  django-admin startproject projectname
or
python (fullpath) startproject projectname

after the sucessful exicution of above commnd django will create a folder in specific location with given project name as folder name 
the folder architechture will looks like bellow





manage.py file:
this file is known as django utility file which is used to perform any kind of operation on perticular project
creation of database, refreshing the database, creating an application, creating super user......etc

urls.py file:
this file in known as url mapping file which contains list of urls and there appropiate 

settings.py file:
this file contains all the settings which are related to a django project like database setting, application setting,time setting ........

wsgi.py file:
wsgi stand for web service(server) guieded inteface
this file is used to intigrate django with 3party service 

note:django come with an inbuilt database that is SQlite3

creating database:
to create a database in django we should set the datbase settings first 
all the database settings will lies databases coloum under settings.py file 
the database setting were rep by , 
name: rep the name of the database with full path 
engine: engine rep type of the database 
host:host rep the place where the datbase exits 
username: valid username used to access the data
password: valid password used to access the data
default database settings:


after the setting the this settings we should run the below commands to create ao refresh tha data 
python manage.py makemigrations

python manage.py migrate

note: make migration commands will always looks for the changes in db(database)
migrate command commite the chages to the database 

creating superuser:
run thr below command to create a super user for django project 

command--->>>  python manage.py createsuperuser
after the exicuting the above command django will ask u for the details like user name, email , password, conform password 
after sucessful creation a superuser record will be stored in auth_user table

"""

"""
application creation:


an application is sublayer of project which contains the major tools of application loke front end , back end, programe language
to create an application which associate with a project use django utility file like below 
--->>> python manage.py startapp appname
after the sucessful exicution of above step django will create a folder under project directory with the name given in above command 
the final architecture show like below






models.py:
it rep data obstraction layer
views.py:
this file rep the business logic layer which contains the logical python function writen based on customer request 
tests.py:
this file contains the test cases writen on top of logical functions 
admin.py:
this file is used to handle django administration portal 
changing the port 
--->>> python manage.py runserver 2000

running a server:
to exicute any django project we need a browser and a server IP address
to create a server IP address for specific django project we will use django utility file
run the below command to start django development server 
to run django in local IP --->>>python manage.py runserver (url=127.0.0.1:8000)
to change the port no of local IP post --->>> python manage.py runserver (port) 2000
to run django development sever in intranet--->>> python manage.py runserver IP:port(127.0.0.1:2000)
to ip address in ubuntu: ifconfig
to ip address in windows : ipconfig

accessing admin portal: 
to access the admin portal use /admin extention url
this url to navigate the user to admin login page where we can perform diff operation to control complete 

mapping application with the project:
follw the below steps to map the application with the project 
1.copy the application name 
2. open settins.py file 
3.locate INSTALL_APPS settings
4.append the application name as string to the setting
5.now django will be able to access application changes 


"""

"""
data base design:
1.creating a table:
in django a table will rep with a Model and 1 model will rep with a class therefore 1 table can be created by creating django
the class which inherites 'models.Model' will be treated as a table 
here the class name will be table name and the syntax looks like below
-->>> class tablename(models.Model):
			field1=data type
			filed2=data type
Note: a table is a combination of diff coloumns and each coloumns rep by a django model field

models field:
1.IntigerField: IntigerField is used to store the numarical values ranging from -2147483648 to +2147483647
IntigerField is avalable at django.db.models.IntigerField
usage:--->>> models.IntigerField()

2.DecimalField:
DecimalField is used to define and store a decimal kind of value with specific no.of numarical and decimals
DecimalField is avalable at django.db.models.DecimalField
this field req 2 mandetory para they are max_digits(which rep no of numarical values) and deciaml_places(which rep no.of floating values)
usage:--->>> models.DecimalField(max_digits,decimai_places)

3.CharField:
this field is used to store the string format of data with specific char size
this field req 1 mandetory para that is max_length
usage:--->>>models.CharField(max_length=value)

4.EmailField:
this field is used to store email addresses with proper inbuilt email valudation 
and it is avalable at django.db.models.EmailField
usage:--->>>models.EmailField(max_length)

5.DateTimeField:
this field is used to store DateField along with time data 
it is avalable at django.db.models.DateTimeField
usage:--->>>models.DateTimeField
auto_now=True
auto_now_add=True
this method takes 2 parameters auto_now rep last seen and auto_now_add rep creation 

URLField:
--->>> link = models.URLField(max_length=500, blank=True, default='')
FileField:
AutoField:
TextField:
ImageFiels

ForeignKey:
--->>> artist = models.ForeignKey(Musician, on_delete=models.CASCADE)



"""


"""
DB Operations:
to perform data base operation django provides 4 methodologies they are 
1.admin portal
2.db tools
3.orm
4.writing queries

using admin portal:
to perform db operations from admin portal that table should register with admin site 
follow the below process to register table with admin portal 
open admin.py file 
import your table name
	from application_name.models import table
	ex:from App.models import person

register the table using below command 
	admin.site.register(tablename)

note: by using register method 1 table can register at a time 
	  each record will be save in the database with tha name as 'tablename object'
	  to change the default table name object with specific name use unicode method inside specific model
syntax:def __unicode__(self):
			return str(self.fieldname)


ORM:(object relational mapping)
which is used to create a mapping btw a class objects and relational database 
ORM concepts will work based on model manager (objects), which is used to perform curd operatoin 
model manager contains 4 major functions which are responsable for performing curd operation 
they are 1.all 2.create 3.filter 4.get
1.all:this method will return all the records from given table in the form of list of objects 
each objects is equivalent to 1 record 
no parameters requier 
o/p is list 
syntax: table_name.objects.all()
we can access the data from each objects by using sub level accessing 
syntax: object_name.field_name
all the orm concepts will exicutes from either views are shell prompt
to open shell prompt run the below command
--->>python manage.py shell

2.Create:
this method is used to insert 1 record into database table
we need to pass the table fields and appropiate values to create method 
after creating an object use save method to save the change permintly
syntax: obj=tablename.objects.create(f1=v1,f2=v2,......)
obj.save()

or

obj=tablename(f1=v1,f2=v2,......)
obj.save()


"""

"""
Filter:
this method will return list of table objects from database based on given condition 
this method takes 1 para that is condition or conditions 
op is always list of objects 
use assignment operator as a parameter while creating the condition 
to work with other compariotion operators use below extentions (sub level)
__lt  lessthan
__gt  greaterthen
__lte lessthan are equal
__gte greater then equal 
__startswith  startswith
__

note: filter method will work both unique and non unique fields
obj=person.objects.filter(age__lt=26)






get:
this method will works like filter but it should return exactly one 
that means we should place condition which matches with exactly one objects



obj=person.objects.get(age=26)
op--one person 
obj=person.objects.get(age__lt=26)
op--MultipleObjectsReturned: get() returned more than one person -- it returned 3!

Example:

>>> obj=person.objects.get(age=26)
>>> obj
<person: vijay>
>>> obj.first_name
u'vijay'
>>> obj.first_name = 'kumar'
>>> obj.save
<bound method person.save of <person: kumar>>
>>> obj.save()
>>> obj.delete()
(1, {u'App.person': 1})

use variable assignment process to update perticular record and save without fail (use save method)
to delete specific objects use delete method 
obj=person.objects.get(age=24)
obj.age=30--->>updating
obj.save()--->>saving
obj.delete()-->>delete

Qmodels:
Q models are used to work with multiple conditions in ORM quiries 
Q models are avalable at django.db.models
 from django.db.models import Q

while writing multiple conditions we should enclosed every condition with Q method 
use & to write and operator | for or operator 

Example: 


>>> obj=person.objects.filter(Q(age__lt=26)&Q(user_name__startswith='p'))
>>> obj
[<person: p>]
>>> obj.first_name
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'first_name'
>>> obj=person.objects.filter(Q(age__lt=26)&Q(user_name__startswith='p'))
>>> obj
[<person: p>]
>>> obj=person.objects.filter(Q(age__lt=26)\Q(user_name__startswith='p'))
  File "<console>", line 1
    obj=person.objects.filter(Q(age__lt=26)\Q(user_name__startswith='p'))
                                                                        ^
SyntaxError: unexpected character after line continuation character
>>> obj=person.objects.filter(Q(age__lt=26)|Q(user_name__startswith='p'))
>>> obj
[<person: siva>, <person: p>, <person: g>]



query = Members.objects.all().query
query.group_by = ['designation']
results = QuerySet(query=query, model=Members)


data = TableNAme.objects.all().group_by('age')




>>> from django.db.models import Q
>>> obj=person.objects.filter(Q(age__lt==26)&Q(user_name__startswith='p'))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'age__lt' is not defined
>>> obj=person.objects.filter(Q(age__lt=26)&Q(user_name__startswith='p'))
>>> obj
[<person: p>]
>>> obj.first_name
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'first_name'
>>> obj=person.objects.filter(Q(age__lt=26)&Q(user_name__startswith='p'))
>>> obj
[<person: p>]
>>> obj=person.objects.filter(Q(age__lt=26)\Q(user_name__startswith='p'))
  File "<console>", line 1
    obj=person.objects.filter(Q(age__lt=26)\Q(user_name__startswith='p'))
                                                                        ^
SyntaxError: unexpected character after line continuation character
>>> obj=person.objects.filter(Q(age__lt=26)|Q(user_name__startswith='p'))
>>> obj
[<person: siva>, <person: p>, <person: g>]
>>> obj=person.objects.all()
>>> obj
[<person: siva>, <person: p>, <person: g>]
>>> for i in obj:
...   print obj.sage
... 
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'QuerySet' object has no attribute 'sage'
>>> for i in obj:
...   print obj.age
... 
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'QuerySet' object has no attribute 'age'
>>> for i in obj:
...   print i.age
... 
25
24
25
>>> obj=person.objects.all().order_by('age')
>>> 
>>> for i in obj:
...   print i.age
... 
24
25
25
>>> obj=person.objects.all().order_by('-age')
>>> for i in obj:
...   print i.age
... 
25
25
24
>>> obj=person.objects.all().group_by('age')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'group_by'
>>> obj=person.objects.all().groupby('age')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'groupby'
>>> query = person.objects.all().query
>>> query.group_by = ['age']
>>> results = QuerySet(query=query, model=person)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'QuerySet' is not defined
>>> from django.db.models import QuerySet
>>> results = QuerySet(query=query, model=person)
>>> results\
... 
[<person: siva>, <person: p>, <person: g>]
>>> for i in results:
...   print i.age
... 
25
24
25
>>> from django.db.models import Max
>>> from django.db.models import Avg\
... 
>>> query = person.objects.all().aggregate(Avg('age'))
>>> query
{'age__avg': 24.666666666666668}
>>> query = person.objects.all().aggregate(Max('age'))
>>> query
{'age__max': 25}
>>> query = person.objects.all().count()
>>> query
3
>>> len(person.objects.all())
3
>>> 


"""