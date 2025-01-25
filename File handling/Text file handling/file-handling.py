'''
File Handling - methodologies to work with diff set of file extension in python


Python has several functions for
creating, reading, updating, and deleting files.

The open() function takes two parameters; filename, and mode.
most used method to open an file in python

open() syntax
syntax1 - open(filename.ext, operation/mode) - open(hello.txt,r)


r: open an existing file for a read operation.
w: open an existing file for a write operation.
    If the file already contains some data, then it will be overridden
    but if the file is not present then it creates the file as well.
a: open an existing file for append operation.
    It won’t override existing data.
r+: To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
w+: To write and read data. It overwrites the previous file if one exists,
    it will truncate the file to zero length or create a file
    if it does not exist.
a+: To append and read data from the file. It won’t override existing data.
"x" - Create - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
syntax2 - open(filename.ext, operation/mode_combined_with_file type(text/binary))
eg - open(hello.txt, rt) or open(hell.txt,rb)

'''
#normal reading an file
file = open("samplefile.txt", "r")
content = file.read() #read() - returns the entire content as a string.
print(content)
file.close()
 
#using system path of that particular file location.
file = open("C:/Users/gs1-harinim/Downloads/Harini_Study materials/File handling/samplefile.txt", "r")
content = file.read()
print(content)
file.close()
 
#reading an file in binary format
file = open("samplefile.txt", "rb")
content = file.read()
print(content)
file.close()
 
 
#writing an file
#if we use 'a' append mode / 'w' mode in python for writing, even tho if file is not present,
#it'll create a new file and save the content
 
#write method will override the entire content
file = open("write sample.txt", "w")
file.write("Hello, World! from Write")
file.close()
 
#append method will only add the content in the last line
file = open("writesamplefile.txt", "a")
file.write("Hello, World! from Append")
file.close()
 
file = open("samplefile.txt", "r")
content = file.read()
print(content)
file.close()
 
 
#using try finally
file = open('samplefile.txt', 'r')
try:
    content = file.read()
    print ("Closed or not: ", file.closed)
    print ("Opening mode: ", file.mode)
    print(content)
finally:
    file.close()
 
#using with statement
#with is newest form of handling exception
#that unlike the first two implementations,
#there is no need to call file.close() when using with statement
print("with statement")
with open("samplefile.txt", "r") as file:
    content = file.read()
    print(content)
    print ("Opening mode: ", file.mode)
    print ("Closed or not: ", file.closed)
print ("Closed or not: ", file.closed)
 
#readline() , reads one by one lines in the file
with open("samplefile.txt", "r") as file:
   line = file.readline()
   i=0
   print("total lines:",line)
   while line:
      print(i,line, end='')
      line = file.readline()
      i+=1
 
#readlines() , reads entire content as splited into list
with open("samplefile.txt", "r") as file:
   line = file.readlines()
   i=0
   print("total lines:",line)
print("")
 
#using wirtelines() , it'll take an list of strings as input and write/append.
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "a") as file:
   file.writelines(lines)
   print ("Content added Successfully!!")
