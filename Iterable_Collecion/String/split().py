#Method 1:
str = " My name is Harini"

#using the split function without passing parameters. This automatically splits the string based on whitespace.
print("split function without passing parameters:",str.split())
Fruits = "Apple**Orange**Mango**Pomogranatte"
#split the string based on some common parameter.
print("split the string based on some common parameter which is ** :",Fruits.split('**'))

#Method 2:
#Split based on max split(optional) parameter:
print("Max split with 0:",Fruits.split('**',0))
print("Max split with 1:",Fruits.split('**',1))
print("Max split with 2:",Fruits.split('**',2))
print("Max split with 3:",Fruits.split('**',3))
print("Max split with 4:",Fruits.split('**',4))
print("Max split with 5:",Fruits.split('**',5))

#Rsplit function:
#using the rsplit function without passing parameters.
print("#using the rsplit function without passing parameters :",Fruits.rsplit())
#rsplit the string based on some common parameter.
print("split the string based on some common parameter which is ** :",Fruits.rsplit('**'))
#Split based on max split(optional) parameter:
print("Max split with 0 for rsplit():",Fruits.rsplit('**',0))
print("Max split with 1 for rsplit():",Fruits.rsplit('**',1))
print("Max split with 2 for rsplit():",Fruits.rsplit('**',2))
print("Max split with 3 for rsplit():",Fruits.rsplit('**',3))
print("Max split with 4 for rsplit():",Fruits.rsplit('**',4))
print("Max split with 5 for rsplit():",Fruits.rsplit('**',5))
#Splitlines()
x = " I \n love \n my \n family\n"
y = x.splitlines()
print("Printing X where \n is applied :",x)
#When This is applied, The string is split based on '\n'
print("Use of splitlines function on X :", x.splitlines())

