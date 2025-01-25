print("***Multiple Inheeritance with Constructor***\n")
#creating base class 1
class Fruits:
    def __init__(self,price,quantity):#creating constructor for base class 1
        #Assigning values to constructor
        self.price = price
        self.quantity = quantity
#creating base class 2
class Vegetables:
    def __init__(self,quality,color):#creating constructor for base class 2
        #Assigning values to constructor
        self.quality = quality
        self.color = color
#creating derived class and dervied class inheriting base class 1 and base class 2
class FruitsVegetables(Fruits,Vegetables):
    #creating constructor for derived class
    def __init__(self,price,quantity,quality,color):
        #calling the base class 1 and 2 and its constructor
        Fruits.__init__(self,price,quantity)
        Vegetables.__init__(self,quality,color)
    def Zepto(self):#defining a function for derived class
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Quality of Vegetable is :",self.quality)
        print("Color of Vegetable is :",self.color)
#creating objects
obj = FruitsVegetables(200,2,"good","Green")
#calling derived class function
obj.Zepto()
print("***Multiple Inheeritance without Constructor***\n")
#creating base class 1
class Fruits:
    price =100
    quantity =1
    def MyFruits(self): #defining func for base class 1
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
#creating base class 2
class Vegetables:
    quality = "excellent"
    color = "yellow"
    def MyFruits(self):#defining func for base class 2
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
#creating derived class and dervied class inheriting base class 1 and 2
class WithoutConstructorFruits(Fruits,Vegetables):
    origin = "Ooty"
    def WithoutConst(self):
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Quality of Vegetable is :",self.quality)
        print("Color of Vegetable is :",self.color)
        print("Origin of Fruits and Vegetables :",self.origin)
      
#creating objects
obj = WithoutConstructorFruits()
#calling derived class function
obj.WithoutConst()