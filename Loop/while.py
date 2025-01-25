'''
intialization
condition
increment/decrement
'''

n = 10

i = 0
while(i<n):
    print(i,end=' ')
    i+=1

#this wont work , because i is 10 from the last program , so we had to re-initialize i
while(i<n):
    if(i==3):
        break
    print(i,end=' ')
    i+=1
print("")

i=0
while(i<n):
    print(i,end=' ')
    if(i==3):
        break
    i+=1
print("")



#infinite condition with break
# while True / while 1 both are same for infinite/recursive action
i = 0
while True:
    print("hello")
    if(i == 3):
        break
    i+=1

  
#infinite condition in while
#while(1):
#    print("hello")

#wont work, because by default we wont have an iterator in while, we need to iterate
l=[1,2,3,4]
while x in l:
    print(x)
    
    


