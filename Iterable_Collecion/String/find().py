'''
method 1 - string.find(substring(required))
method 2 - string.find(substrig,start_pos(optional),end_pos(optional))
'''
str = "Hello World"

print("***find()***")

#Method 1  - string.find(substring(required))
print("Method 1 of just passing the substring alone as parameter :",str.find("l"))

#Method 2 - string.find(substrig,start_pos(optional),end_pos(optional))
print("Method 2 of passing the substring,start and end pos as parameter :",str.find("l",3,6))

#If the substring is not present in the string
print("When the substring is not present in the string :",str.find("a"))

print("***rfind()***")

#Rfind() returns the right most first occurence of the given character in a string.

#Method 1  - string.rfind(substring(required)). 
print("Method 1 of just passing the substring alone as parameter for rfind() :",str.rfind("o"))

#Method 2 - string.rfind(substrig,start_pos(optional),end_pos(optional))
print("Method 2 of passing the substring,start and end pos as parameter for rfind() :",str.rfind("l",3,6))

#If the substring is not present in the string in rfind()
print("When the substring is not present in the string for rfind() :",str.rfind("a"))
