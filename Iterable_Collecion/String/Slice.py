'''
Syntax- string[start pos : end pos : step]
                [A]
        string[slice(start pos,end pos,step)]
'''
str = "Hello  World"
print(str) #prints the string
print(len(str)) # prints the length of the string
print(str[0:]) # prints the string starting from first character till end.
print(str[:4]) # prints the string from the first character till 4th character.
print(str[-7:-2]) #prints the characters from right(Second character).

#To revere a string
print(str[-1:-(len(str)+1):-1]) # prints str in reverse
print(str[::-1]) # reverse a string
print(str[-1:-(len(str)+1):-1]) #reversing the string using dynamic approach


# using slice function
print(str[slice(0,13,-1)]) #prints the characters from right
print(str[slice(0,8,2)]) #prints the characters from the first position with the step 2.
print(str[slice(0,8,3)]) #prints the characters with the step 3 from 0th character till 12th character


