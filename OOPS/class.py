#creating a class
class MyCollege:
    a = 100 #Static variable creation
obj = MyCollege() #creating an object
print("Creating and accessing an object within the class:",obj.a)

#using __init__():
#defining a class
class Student:
    #creating constructor
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department
#creating objects
o = Student("Harini",23,"CSE")
o1 = Student("Thaarun",23,"IT")
print("Objects of the class are:",o.name,o.age,o.department) #calling the objects

#using __str__():
#defining a class
class Student:
    #creating constructor
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department
    def __str__(self): #used to format the class to a user desired data type
        return f"{self.name},{self.age},{self.department}"
#creating objects
o = Student("Harini",23,"CSE")
o1 = Student("Thaarun",23,"IT")
print("Objects of the class are:",o1) #calling the objects directly without passing the arguments