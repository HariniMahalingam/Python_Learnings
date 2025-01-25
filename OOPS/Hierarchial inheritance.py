print("***Hierarchial Inheritance with Constructor***\n")
class Fruits:#creating base class
    def __init__(self,price,quantity):#creating constructor for base class 1
        #Assigning values to constructor
        self.price = price
        self.quantity = quantity
class Vegetables(Fruits):#creating derived class 1
    def __init__(self,price,quantity,quality,color):#creating constructor for derived class 2
        #Assigning values to constructor
        self.quality = quality
        self.color = color
        Fruits.__init__(self,price,quantity)
    def Swiggy(self):
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Quality of Vegetable is :",self.quality)
        print("Color of Vegetable is :",self.color)
class FruitsVegetables(Fruits):#creating derived class 2
    def __init__(self,price,quantity,region):#creating constructor for derived class 2
        self.region = region
        Fruits.__init__(self,price,quantity) #calling the base class and its constructor
    def Zepto(self):#defining a function for derived class
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Region of Vegetable is :",self.region)
#creating objects
obj = FruitsVegetables(200,2,"Coonor")
obj2 = Vegetables(300,3,"average","green")
obj2.Swiggy()
obj.Zepto()
print("***Hierarchial Inheritance without Constructor***\n")
#creating base class 1
class Fruits:
    price =100
    quantity =1
    def MyFruits(self): #defining func for base class 1
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
class Vegetables(Fruits):#creating derived class 1
    quality = "excellent"
    color = "yellow"
    def MyFruits(self):#defining func for base class 2
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Quality of Vegetable is :",self.quality)
        print("Color of Vegetable is :",self.color)
class WithoutConstructorFruits(Fruits):#creating derived class 2
    origin = "Ooty"
    def WithoutConst(self):
        print("Price of Fruits is :",self.price)
        print("Quantity of Fruits is :",self.quantity)
        print("Origin of Fruits and Vegetables :",self.origin)
      
#creating objects
obj = WithoutConstructorFruits()
obj1 = Vegetables()
#calling derived class function
obj1.MyFruits()
obj.WithoutConst()
