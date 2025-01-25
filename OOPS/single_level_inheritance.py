print("***Single Inheeritance with Constructor***\n")
#With constructor
#creating base class
class Fruits:
    #creating constructor for base class
    def __init__(self,price,quantity):
        #Assigning values to constructor
        self.price = price
        self.quantity = quantity
#creating derived class and dervied class inheriting base class
class Apple(Fruits):
    #creating constructor for derived class
    def __init__(self,price,quantity,origin):
        #calling the base class constructor
        Fruits.__init__(self,price,quantity)
        self.origin = origin
    #defining a function for derived class
    def MyApple(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
        print("Origin of apple is :",self.origin)

#creating objects
obj = Apple(200,1,"Shimla")
#calling derived class function
obj.MyApple()

print("***Single Inheeritance without Constructor***\n")
#Without constructor
#creating base class
class Fruits:
    price =100
    quantity =1
    #creating constructor for base class
    def MyFruits(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
#creating derived class and dervied class inheriting base class
class Apple(Fruits):
    origin = "Ooty"
    def Apples(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
        print("Origin of apple is :",self.origin)
      
#creating objects
obj = Apple()
#calling derived class function
obj.Apples()