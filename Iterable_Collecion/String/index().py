'''
method 1 - string.index(substring(required))
method 2 - string.index(substrig,start_pos(optional),end_pos(optional))
'''
str = "Hello World"

print("***index()***")

#Method 1  - string.index(substring(required))
print("Method 1 of just passing the substring alone as parameter :",str.index("l"))

#Method 2 - string.index(substrig,start_pos(optional),end_pos(optional))
print("Method 2 of passing the substring,start and end pos as parameter :",str.index("l",3,6))

# #If the substring is not present in the string
# print("When the substring is not present in the string :",str.index("a"))

print("***rindex()***")

#Rindex() returns the right most first occurence of the given character in a string.

#Method 1  - string.rindex(substring(required)). 
print("Method 1 of just passing the substring alone as parameter for rindex() :",str.rindex("o"))

#Method 2 - string.rindex(substrig,start_pos(optional),end_pos(optional))
print("Method 2 of passing the substring,start and end pos as parameter for rindex() :",str.rindex("l",3,6))

#If the substring is not present in the string in rindex()
print("When the substring is not present in the string for rindex() :",str.rindex("a"))
