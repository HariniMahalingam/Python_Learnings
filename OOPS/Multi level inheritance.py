print("***Multi level Inheeritance with Constructor***\n")
class Fruits:#creating base class
    def __init__(self,price,quantity):#creating constructor for base class
        #Assigning values to constructor
        self.price = price
        self.quantity = quantity
class Apple(Fruits):#creating intermediate class
    def __init__(self,price,quantity,origin): #creating constructor for intermediate class
        #calling the base class constructor
        Fruits.__init__(self,price,quantity)
        self.origin = origin
    #defining a function for derived class
    def MyApple(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
        print("Origin of apple is :",self.origin)
#creating derived class
class OotyApple(Apple):
    def __init__(self, price, quantity, origin,quality):
        Apple.__init__(self,price,quantity,origin)
        self.quality = quality
    def ooty(self):
        print("Price of Ooty apple is :",self.price)
        print("Quantity of Ooty apple is :",self.quantity)
        print("Origin of Ooty Apple is:",self.origin)
        print("Quality of Ooty Apple is:",self.quality)
obj = OotyApple(2000,20,"Coonor","Outstanding")#creating objects
#calling derived class function
obj.ooty()

print("***Multi-level Inheeritance without Constructor***\n")
#creating base class 
class Fruits:
    price =100
    quantity =1
    #creating constructor for base class
    def MyFruits(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
#creating intermediate class
class Apple(Fruits):
    origin = "Ooty"
    def Apples(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
        print("Origin of apple is :",self.origin)
#creating derived class
class ShimlaApple(Apple):
    region = "Coonor"
    def shimlaapp(self):
        print("Price of Apple is :",self.price)
        print("Quantity of apple is :",self.quantity)
        print("Origin of apple is :",self.origin)
        print("Region of the Apple is :",self.region)
      
#creating objects
obj = ShimlaApple()
#calling derived class function
obj.shimlaapp()