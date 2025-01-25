num_tuple = (1,3,4,2)

#accessing tuples
print("\naccessing via index:",num_tuple[0])
print("accessing tuples using for loop")
#using for loop we can access individual elem of the tuple
for i in num_tuple:
    print(i,end=' ')
print("\n")
#using slice , it will return it as tuple
print("using slice operator: ", num_tuple[0:])
print("\n")
#tuple cannot be updated, once declared
#num_tuple[0]=10
#print(num_tuple)


#updating tuples
#1) converting it to an list and we can use all list operations, then convert back to tuple
x = ("apple", "banana", "cherry")
print("before updating an tuple:",x)
y = list(x)#convert to list
y[1] = "kiwi" #update using index
x = tuple(y) #convert back to tuple
print("updating an tuple via list:",x)
print("\n")
#2) we can add tuple to tuple
x=("a","b","c")
y=("d","e","f")
print("adding tuple to tuple using (+)", x+y)
print("\n")

#upacking tuples
#method 1:
#note: unpack individual variable needs to match len of tuple else error is thrown
a,b,c,d=num_tuple
#a,b = num_tuple wont map the first 2 items of list, it will throw error
print("unpacking list using indivi variable a,b,c,d",a,b,c,d)
#method 2:
#we can unpack with *
#example 1:
a,*b = num_tuple
#maps the a to the first elem of tuple and rest is returned as list mapped to b
print("unpacking using *",a,b)
print("\n")

#example 2:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#tuple[0] is mapped to green
#tuple[last] is mapped to red
#rest all the inbetween elem are returned as list mapped to tropic
(green, *tropic, red) = fruits
print("unpacking tuple using *",green,tropic,red)
print("\n")

#Joining tuples
#1) using +
x=("a","b","c")
y=("d","e","f")
print("adding tuple to tuple using (+)", x+y)
#2) using *
print("using * to multiply the count of tuple", x*2)
print("\n")
#tuple in-built methods

#1) len()
print("len()",len(num_tuple))

#2) count() - count the occurence of elem in the entire list
print("count() the occurence is :", num_tuple.count(3))
print("count() the occurence no such value :", num_tuple.count(23))#no such value

#3) index() - return the first occurence of the value present in the entire list from LtoR
print("index() for the given value:",num_tuple.index(4))

#4) max(),min() finding min, max in lists
print("max() function list",max(num_tuple))
print("min() function list",min(num_tuple))

#5) sum() finding the sum total of the elem in list
print("sum() funciton in list",sum(num_tuple))

#6) sorted() - return the tuple in sorted as list
x = sorted(num_tuple)
print(type(x))

#7) tuple() - method to convert other iterable collection of data to tuple.
num_list = [5,6,7,8]
x = tuple(num_list)
print("converting list into tuple:",x)




"""
Tuple - (), Ordered, Immutable(un-changeable), Allows duplicates
        Additional info
            - once declared tuples cannot be directly changed by accessing index
            - to update an tuple, we need to convert to it list,update and then
            convert it to tuple.
        Methods:
        adding tuple - using *,+ , converting to list
        unpacking tuples - using variable and *
        count()
        index()
        tuple()
        min(),max()
        sorted()
        sum()
        len()
"""



