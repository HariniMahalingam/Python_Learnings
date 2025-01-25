x = "Hello World!"
print(len(x))
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
thisdict = {
  "brand": "Ford",
}
print(len(thisdict))
class Car:#Class polymorhphism
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):#same method name
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model   
  def move(self):#same method name
    print("Sail!")
car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
for x in (car1, boat1):
  x.move()#separate obj is accessed with same method name
