'''
same as file handling concepts, its same logic for excel write and append
2 methods are there for excel writing file.
write
append

'''
from openpyxl import Workbook

workbook = Workbook()

workbook.save(filename="sample.xlsx") #creates an new excel file. ovverrides.

print("file created")


import openpyxl

wb = openpyxl.Workbook() #workbook() creating an new object, means creating an new file

sheet = wb.active

c1 = sheet.cell(row=1, column=1)

# writing values to cells
c1.value = "Hello"

c2 = sheet.cell(row=1, column=2)
c2.value = "World"

c3 = sheet['A2']
c3.value = "Welcome"

# B2 means column = 2 & row = 2.
c4 = sheet['B2']
c4.value = "Everyone"

wb.save("sample.xlsx")
print("file created and values are stored")


#Append mode 

wb = openpyxl.load_workbook("sample.xlsx")
#load_workbook is an method we will be appending the content

sheet = wb.active 

c = sheet['A3'] 
c.value = "New Data"

wb.save("sample.xlsx")
