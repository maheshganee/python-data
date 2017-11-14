"""
file_operation:
python comes with an inbuilt open method which is used to work with text files 
the text files can operated in 3 operation modes they are        read,write,append modes 
open method takes atleast 1 para and atmost 2 para 
1 para rep the file name along with full path and 2 para rep operatin modes 
operation modes rep with single charecter they are 'r' for read, 'w' for write 'a' for append
open method returns a file point of object which contains file name and operaion mode detais

read operation mode:
use 2 para as 'r' to open the file in read operation
when a file open in read mode we can only perform read operation
read operation will applicable only when the file exist

opening file syntax is open('file_name','mode')
fp = open('data.txt', 'r')
print fp

read functions:
  read
  readline
  readlines

read:

this method will return the file data in a string format 
this method takes atmost 1 para that is index position 
the default value of index position is always length of file 
syntax: fp.read(p1).....here p1 is index mode
note: all the read operation function will cause a shifting of file point of causer to rest the file pointer causer we can use seek method

seek:

this method takes exactly 1 para that is index position to reset
fp.seek(index position)

readline:
this method will return 1 line of the file at a time 
this method takes atmost 1 parameter that is index position and the default value is always length of 1 line
syntax: fp.readline(index_position)
print fp.readline(7)

fp = open('data.txt', 'r')
print fp
print fp.read()
fp.seek(0)
print fp.read()
print fp.readline(7)

readlines:

this method will return list of lines in given file
no para req
and op is list of lines

print fp.readlines( )


write operation mode:
use w as 2 para in open function to work with the file in write operation mode
write operation mode will always creates a new file with given name 
in write op mode we can use 2 functions they are       write and writelines

write:this method is used to write 1 string into the given to the file 
write method takes exactly 1 para that is 1 string 
syntax: fp.write('string\n')
op is none

writelines:

this method is used to add multiple string to the given file
this method takes exactly 1 para that is the list of tuple
syntax:fp.writelines([string1,string2,string3...........])

append operation mode: 
to open a file in append open mode use 2 para as a
to work with append operation mode the file exist in the system
we can perform 2 functions in append operation mode which are similar to write operation mode functions
they are write and write lines

write:this method is used to append 1 string into the given to the file 
write method takes exactly 1 para that is 1 string 
syntax: fp.write('string\n')
op is none

writelines:

this method is used to append multiple string to the given file
this method takes exactly 1 para that is the list of tuple
syntax:fp.writelines([string1,string2,string3...........])




"""