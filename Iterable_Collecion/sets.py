'''
Sets - {}, un-ordered, un-changeable, allows dupliactes
Additional info:
    only using iterator we can access sets, not using index function(coz its unordered)

in-built methods:
    adding values to set - add() , update()
    deleting values in set - remove(), discard(), pop(), clear()
    copy()
    len()
    union()
    intersection()
    min(),max(),sum()
    set()
    
'''

num_set = {2,4,3,1}


#duplicates not allowed
thisset = {"apple", "banana", "cherry", True, 1, 2}
print("Ture and 1 are duplicates :",thisset)
thisset = {"apple", "banana", "cherry", False, 0, 2}
print("false and 0 are duplicates :",thisset)

#accessing sets:

#using index we cannot access, since set is unordered
#print("access using index:",num_set[0])

#iterating using index:
#for i in range(len(num_set)):
#    print(num_set[i],end=' ')
    
#iterator is only used for accessing an set
for i in num_set:
    print(i,end=' ')

print("")
#built-in methods:

#1) len()
print("len() -",len(num_set))

#Adding value to sets
#2) add()
print("add() - ", num_set.add(5))

#3) update() - any iteratable collections set, list , tuple , dictionary can be added to an set
x = [6,8,9]
num_set.update(x)
print("update() used for list - ", num_set)
y = {10,7}
num_set.update(y)
print("update() used for another set -",num_set)

#Removing elements from sets
#4)remove() - disadv if element not present is given, it will raise an error
num_set.remove(10)
print("after using remove() -", num_set)

#5) discard() - even tho element not present is given , error is handled.
num_set.discard(10)
print("after using discard() -", num_set)

#6)pop() - since set is unorder, if we use pop it'll remove random elements
thisset = {"apple", "banana", "cherry"}
print("before using pop() - ",thisset)
x = thisset.pop()
print("random elem for removing is -",x)#prints the elem removed from set
print("After using pop() random elem removed is - ",thisset)

#7) clear() - removed all the elements in the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("after using clear() set-",thisset)


#8) copy() - copy one set to another set.
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print("copy() - ",x)

#9) set() - method to convert any iteratble collections list,tuple to set
x = [1,2,3,4]
y = set(x)
print("using set()",type(y),y)

#10) intersection() - returns a new set with the common value of given 2 sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("intersection() used between two sets",z)

#11) union() - joins/adds two sets and returns a new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) 
print("union() joining/adding two sets-",z)

#12) min(),max(),sum()
print("min() of set -",min(num_set))
print("max() of set -",max(num_set))
print("sum() of set -",sum(num_set))
