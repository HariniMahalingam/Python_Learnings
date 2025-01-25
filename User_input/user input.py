# Get the input from the user as a integer.
print("Get the input from the user as integer")
x = int(input("Enter an integer :"))
print("Add 10 to integer:",x+10)
print(" ")

# Get the input from the user as a string.
print("Get the input from the user as a string")
y=input("Enter a string :")
print("Strip the first three characters of the string:",y[0:3])
print(" ")

# Get the list of integers from the user as a string - Method 1 using for loop
print("Get the list of integers from the user as a string - Method 1 using for loop:")
z = int(input("Enter the range :"))
lis = []
for i in range(z):
    a = int(input("Enter the numbers:"))
    lis.append(a)
print("the final list is :",lis)
print(" ")

# Get the list of integers from the user as a string - Method 2 using unpacking
#drawback - the given integer value will be of string data type, since we have used input()
print("Get the list of integers from the user as a string - Method 2 using unpacking to overcome for loop but limited based on size")
m,n =(input("space separated integer values:")).split()
print("separated as m,n:",m,n)
print("Type of m and n:",type(m),type(n))
print(" ")

#splitting using map to overcome the above mentioned drawback
#drawback, only for static 2 variable approach this will work , if dynamically the length changes, we cannot achieve it
#map(function,iterable) is the syntax , so we approach this logic and achieve output.
print("Get the list of integers from the user as a integer - Method 3 using unpacking to overcome the str to int conversion")
i,j = map(int,(input("space separated integer values:")).split())
print("separated as i,j:",i,j)
print("Type of i and j:",type(i),type(j))
print(" ")

#splitting and getting the input using list,map to overcome the above mentioned drawback
print("Get the list of integers from the user as a integer - Method 4 using unpacking to overcome the size restrictions")
k = list(map(int,(input("space separated integer values:")).split()))
print("separated as k:",k)
print("Type of k:",type(k))
print(" ")