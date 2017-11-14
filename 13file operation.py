"""
file operation:python comes with an inbuilt open method which is used to work with text files
//the text files can operated in three operation modes they are
read
write
append

//open method takes atleast one parameter and atmost two parameters
//first parameter represents the file name along with full path and second parameter represents operation modes
//operation modes represents with single carrcter they are r for read w for write a for append
//open method returns a file pointer object which contains file name and operation mode details

read operation mode-------use second parameter r to open the the file in read operation mode
//when a file opened in read mode we can only perform read operations

so read operation will applicable only when the file exit

syntax-----open('file name,'mode)

ex------fp = open('data.txt','r')

read functions

1 read
2 readline
3 readlines

read----this method will return the file data in a string format
//this method takes atmost one parameter that is index position
//the default value of index position is always length of the file

syntax-----fp.read(index position)

note ------all the read operation function will cause a shifting of file pointer courser
to reset the file pointer courser we can use seek method

seek------this method takes exactly one parameter that is index position to reset

syntax-----fp.seek(index position)


readline-------this method will return one line of the file at a time
//this method takes atmost one parameter that is index position and default value is first line of file


syntax-----fp.readline(index position)


readlines--------this method will return list of lines in given files
//no parameters required
//output is always list

syntax-----fp.readlines()


2.write operation mode------use w as second parameter in open function to work with the files in write operation
//w o m will always creates new file with given name
//in write operation mode we can use two functions they are
write
writelines

write-------this method is used	to write one string into the given file
//write method take exactly one parameter that is one string


syntax-----fp.write()


writelines-------this method is used to add multipule strings to given file
//this method takes exactly one parameter list r tuple

syntax-----fp.writelines()


3.append operation mode-------use a as second parameter in open function to work with the files in append o m
//to work with a o m the file should exit in the system
//we can perform two functions in a o m which are similar to write operation mode
they are 
write
writelines


rb  --------read + binary(read + append)
rb+---------read + append/write
wb----------write +read
wb+---------write+raed+append





"""

fp = open('/home/mahesh/Desktop/data.txt','w')
fp.write('hi')
