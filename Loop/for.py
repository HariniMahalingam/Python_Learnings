str = "Harini"
lis = [1,2,3,4,5]
tup = ["t","u","p","l","e"]
set = {"a","2","c","4","e","6"}
dict = {"name":"harini","age":23}
num = 5
'''
syntax -
-for(end(required))
-for(start(optinal),end,inc(optional))
'''
print("***FOR LOOP WITH INTEGER***")
#for loop with num using range
for i in range(0,num):
    print(i,end=" ")
print("\n")
for i in range(num):# end value is mandatory,start is optional;
    print(i, end =" ")
print("\n")
for i in range(0,num,2):
    print(i,end= " ")
print("\n")
print("***FOR LOOP WITH STRING***")
for i in range(0,len(str)):
    print(i,end=" ")
print("\n")
for i in range(len(str)):
    print(i,end=" ")
print("\n")
for i in range(0,len(str),2):
    print(i,end=" ")
print("\n")
for i in str:
    print(i,end=" ")
print("\n")
print("FOR LOOP WITH LISTS***")
for i in range(0,len(lis)):
    print(i,end=" ")
print("\n")
for i in range(len(lis)):
    print(i,end=" ")
print("\n")
for i in range(0,len(lis),2):
    print(i,end=" ")
print("\n")
for i in lis:
    print(i,end=" ")
print("\n")
print("***FOR LOOP WITH TUPLES***")
for i in range(0,len(tup)):
    print(i,end=" ")
print("\n")
for i in range(len(tup)):
    print(i,end=" ")
print("\n")
for i in range(0,len(tup),2):
    print(i,end=" ")
print("\n")
for i in tup:
    print(i,end=" ")
print("\n")
print("***FOR LOOP WITH SETS***")
for i in range(0,len(set)):
    print(i,end=" ")
print("\n")
for i in range(len(set)):
    print(i,end=" ")
print("\n")
for i in range(0,len(set),2):
    print(i,end=" ")
print("\n")
for i in set:
    print(i,end=" ")
print("\n")
print("***FOR LOOP WITH DICTIONARY***")
for i in dict:
    print(i,end=" ") #returns only the keys
print("\n")
print("***FOR LOOP WITH BREAK***")
print("\n")
for i in range(num):
    print(i,end=" ")
    if i==5:
        break
print("\n")
print("***FOR LOOP WITH PASS***")
for i in range(num):
    print(i,end=" ")
    if i==5:
        pass
print("\n")
print("***FOR LOOP WITH CONTINUE***")
for i in range(num):
    print(i,end=" ")
    if i==5:
        continue
print("\n")
#reverse in for loop
for i in range(num,0,-1):
    print(i,end=' ')
print("\n")
#nested for loop - parent->child (or) 2X2 matrixes
for i in range(3):
    for j in range(3): 
        print(i+j,end='')
    print("")