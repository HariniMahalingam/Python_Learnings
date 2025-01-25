"""
startswith - used to return the 'true/false' if the given substring to be searched is present in string.
syntax
method 1 - string.startswith(substring(required))
method 2 - string.startswith(substrig,start_pos(optional),end_pos(optional))
method 3 - string.startswith(tuple(strings),start_pos(optional),end_pos(optional))
            we can also give an tuple of strings and check if the string startswith any one substring of that given tuple 
"""
str = "Hello World,Welcome to Python!"
#method 1 passing only substring
print("Substring alone:",str.startswith("llo"))
#method 2 passing substring, start pos, end pos
print("Giving start and end pos:",str.startswith("World",6))
#method 3 passing a tuple of strings as substr
print("Tuple of strings as substr",str.startswith(("World","to","Python"),6,30))