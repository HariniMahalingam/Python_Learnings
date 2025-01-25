print("***Use of super()***\n")
#creating base class 2
class Vegetables:
    def __init__(self,quality,color):#creating constructor for base class 2
        #Assigning values to constructor
        self.quality = quality
        self.color = color
#creating derived class and dervied class inheriting base class 1 and base class 2
class FruitsVegetables(Vegetables):
    #creating constructor for derived class
    def __init__(self,quality,color,region):
        self.region = region
        #calling the base class 1 and 2 and its constructor
        super().__init__(quality,color)
    def Zepto(self):#defining a function for derived class
        print("Quality of Vegetable is :",self.quality)
        print("Color of Vegetable is :",self.color)
        print("Region of Vegetables is :",self.region)
#creating objects
obj = FruitsVegetables("good","Green","Madurai")
#calling derived class function
obj.Zepto()
