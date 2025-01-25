"""
endswith - used to return the 'true/false' if the given substring to be searched is present in string.
syntax
method 1 - string.endswith(substring(required))
method 2 - string.endswith(substring,start_pos(optional),end_pos(optional))
method 3 - string.endswith(tuple(strings),start_pos(optional),end_pos(optional))
            we can also give an tuple of strings and check if the string endswith any one substring of that given tuple 
"""

str = "I am Harini and I am working as Data Scientist"
#method 1 where substring is used.
print("Substring alone:",str.endswith("Scientist"))
#method 2 where substring,start position and end position is used.
print("Giving start and end pos:",str.endswith("Data",32,36))
#method 3 where tuple of strings
print("Giving tuple of strings:",str.endswith(("working","am","Data"),1,46))