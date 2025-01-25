l = [1,2,3,"a","b","c",4,5,6]

# Accessing the elements in the list using slice operator.
print("Accessing the list using slice operator :",l[2])
print("\n")
# Accessing the elements in the list using for loop
print("Accessing the list using for loop :")
for i in l:
    print(i,end="")
print("\n")

#Updating the list.
l[6]=7
print("Updated list :",l)
print("\n")

#list can be nested list
#list as nested list(looks similar to JSON)
employees = [
     {"name": "John", "age": 30, "job": "Software Engineer"},
   {"name": "Alice", "age": 25, "job": "Web Developer"},
   {"name": "Bob", "age": 45, "job": "Data Analyst"},
 ]
#Accessing the elements using nested list.
for i in employees:
    for j in i:
        print(j,end=",")
    print("\n")
#accessing nested list using index
print("accessing list directly using index: ",employees[2]["name"])
print("\n")

#Unpacking lists
#Method 1:Static method - unpacking lists based on the size of list.
a,b,c,d,e,f,g,h,i = l
print("Unpacking the lists using static method",a,b,c,d,e,f,g,h,i)
# Method 2:Dynamic method - unpacking lists randomly without knowing the size of the list.
x,*y = l
print("Unpacking the lists using dynamic method :",x,y)
print("\n")

#Built in functions in list:
# Adding the elements to the list
# len() - used to find the length of the list.
print("Length of the list :",len(l))
print("\n")
# append() - adding an element to the end of the list.
a=l.append(5)
print("Using append() in list:",l)
print("\n")
# insert() - add an element based on some index in the list.
b=l.insert(3,5)
print("Insert() in the list :",l)
print("\n")
#extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("extend() will concat two lists:",list1)
print("\n")

# Deleting elements in the list.
# Remove() - removes the elements in the list in the first occurence from Left to right.
c = l.remove(5)
print("Remove the elements from L to R in the first occurence using remove():",l)
print("\n")
# Pop() - removes the element in the list in the specified index.
d = l.pop(5)
print("Remove the elements using pop() at the specified index :",l)
print("\n")
# clear() - clears the elements in the list.
print("Clears the elements in the list using clear() :",l.clear())
print("\n")

#copying a list
#copy()
lis = [1,2,4,5,6,2]
copy_list = lis.copy()
print("copy() used to copy an list into new list;",copy_list)
print("\n")

# min and max()
print("Minimum in the list l :",min(lis))
print("Maximum in the list :",max(lis))
print("\n")
# sum,count and index()
print("Sum of the list l:",sum(lis))
print("Count the occurences of 3 in the list :",lis.count(2))
print("Index of the element 5 in the list :",lis.index(5))
print("\n")

# Reverse and reversed()
print("Reversing the list using reverse():",lis.reverse())
print("Reversing the list using reversed():",list(reversed(lis)))
# Reversing the list using slice operator
print("Reversing the list using slice operator :",lis[::-1])
print("\n")

# sort and sorted()
print("Reversing the list using sort():",lis.sort())
print("Reversing the list using sortd():",list(sorted(lis)))
print("\n")

#map()
res = list(map(lambda x: x*2, lis))
print("map() function changing the value:",res)
res = list(map(float, lis))
print("map() function changing the data type:",res)
print("\n")

#filter()
result = list(filter(lambda x: x%2 == 0, lis))
print("filter() function:",result)
res = list(filter(lambda x: x*2, lis))
print("using map logic to filter(but did not work):",res)
print("\n")

#append() can also be user by iterating the second list and appending to the first list
#slicing array opreator can also be used to concat second list to first list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1[len(list1):]=list2
print("concat using slice array operator:",list1)
print("\n")