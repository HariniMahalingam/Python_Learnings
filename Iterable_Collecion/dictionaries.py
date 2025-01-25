'''
dictonaries - {key:value}, ordered, mutable(changeable), no duplicates(since unique key is present)
    Additional info:
    using update(), updating the dictinary if the key mentioned is not present, it will add it as new key(wont throw error)
    in-built methods:
        keys()
        get()
        update()
        pop()
        popitem()
        clear()
        values()
        items()
        copy()
'''

#proof of duplicates not allowed
dict_value = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("duplicates not allowed, even tho we have two same key with diff values",dict_value)

#Accessing dictionaries

# 1) usally other iterable collections, we use [index], here we specify [key] (even more specific access)

dict_value = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict_value["model"]
print("accessing using key-",x)

#2) using get() - function will return the value of the given key

x=dict_value.get("brand")
print("accessing using get()-",x)

#3) keys() method will return a "list" of all the keys in the dictionary.

x=dict_value.keys()
print("using keys()-",x)


#Updating new item/key to an existing dictionaries

#1) Method 1: directly changing the value using key:
dict_value = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict_value["year"] = 2018 #key-year value is updated.
print("updated dic-",dict_value)

#2) Method 2: using update() function
#if we giv key(which is not already present in dic, it wont throw error) rather it will add it as new key.
dict_value = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict_value.update({"year": 2020})#passing key:value to the dictionary and updating.
print("using update(), dic value-",dict_value)

#Adding new item/key to an dictionaries

# 1) Method 1:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print("before adding an key-",x) #before the change
car["color"] = "white"
print("after adding an key, checking whether it refelected in original dict-",x) #after the change

#2) Method 2: using update() function
#if we giv key(which is not already present in dic, it wont throw error) rather it will add it as new key.
dict_value = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict_value.update({"year": 2020})#passing key:value to the dictionary and updating.
print("using update(), dic value-",dict_value)


#Removing from dictionaries
#1) pop() - syntax dictinoary.pop(key(required))
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")#pop() must require 1 arg as key to be removed, else without arg error will be thrown.
print("using pop()-",thisdict)

#2) popitem() - removes the lastly added key to dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "white"#last added key is color.
thisdict.popitem()
print("using popitem() after removing last added key",thisdict)

#3) clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print("using clear() clears all keys&values-",thisdict)

#Looping thro dictionaries.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#1) normal for loop: #by default it takes keys()

for x in thisdict:
  print("using basic for loop-",x)
print("")

#since it gives the key , we can access it like this also
#here we get all the values, by direct access using key.
for x in thisdict:
    print("utilizing basic for loop and iterating the value of the dic-",thisdict[x])
print("")

#2) using keys() - return all the keys in dic as list
for x in thisdict.keys():
  print("using keys()-",x)
print("")

#3) using values() - returns all the values in dic as list
for x in thisdict.values():
  print("using values()-",x)
print("")

#4) using items() - return all the keys & values in dic
for x, y in thisdict.items():
  print("using items()-",x, y)
print("")

#Nested Dictionaries
#basic nested declaration
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#efficient way of nested declaration
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Accessing elem in nested declaration
#1) method 1: using index operator
print("using index, accessing the nested dic-",myfamily["child2"]["name"])

#2) method 2: using for loop(we treat it as 2X2 matrix)
#accessed using items()
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])#for loop is iterated with keys()and we access individual elem of child_dic

for x, obj in myfamily.items():
  print(x)

  for k,y in obj.items():
    print(y + ':', k)#for loop is iterated with items(), so we get key and values of child_dic.

#in-built methods in dictionaries

#copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print("using copy()-",mydict)
