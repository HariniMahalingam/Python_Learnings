class College:#base class
    def coll(self):
        print("This is a college")
class Department(College):#derived class inheriting base class
    def dept(self):
        print("There are so many departments in the college")
class ComputerScience(Department,College):# a class inheriting both base class and derived class
    def cse(self):
        print("This is department of CSE")
#creating objects
a = ComputerScience()
#invoking functions of all the class by using the ComputerScience class
a.coll()
a.dept()
a.cse()