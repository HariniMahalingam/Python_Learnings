# Try - except block of code with error
print("Try - except block of code with error")
try:
    print(x)
except:
    print("Value of x is not defined")
print(" ")
# Try - Except block of code without error
print("Try - Except block of code without error")
x=10
try:
    print(x)
except:
    print("Value of x is not defined")
print(" ")
# Try-Except-Except block of code with error for first except block
print("Try-Except-Except block of code with error for first except block")
try:
    print(y)
except NameError:
    print("Value of x is not defined")
except:
    print("Hello world")
print(" ")
# Try-Except-Except block of code with error for second except block
print("Try-Except-Except block of code with error for second except block")
try:
    print(12/0)
except NameError:
    print("Value of x is not defined")
except:
    print("Hello world")
print(" ")
# Try- Except-Except block without error
print("Try- Except-Except block without error")
n=5
try:
    print(n)
except NameError:
    print("Value of n is not defined")
except:
    print("Hello world")
print(" ")
# Try-Except-Else block with error
print("Try-Except-Else block with error")
try:
    print(b)
except:
    print("Value of b is not defined")
else:
    print("value of b is defined")
print(" ")
# Try-Except-Else block without error
print("Try-Except-Else block without error")
z=12
try:
    print(z)
except:
    print("Value of z is not defined")
else:
    print("value of z is defined")
print(" ")

# Try-Except-Finally with error
print("Try-Except-Finally with error")
try:
    print(j)
except:
    print("Value of b is not defined")
else:
    print("value of b is defined")
finally:
    print("Finally, code is completed")
print(" ")

# Try-Except-Finally without error
print("Try-Except-Finally without error")
j=100
try:
    print(j)
except:
    print("Value of b is not defined")
else:
    print("value of b is defined")
finally:
    print("Finally, code is completed")
print(" ")