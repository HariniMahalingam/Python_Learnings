#local and global scope
a=100
def func():
    a=200 #The scope of A is reinitialized and this 200 is applicable only inside func()
    global x
    x=500 #The global keyword is used to set the value across the program and is not restricted only inside the function
    print("A as local scope",a)
    print("X as local scope",x)
func()
print("A as global scope",a)
print("X as global scope",x)