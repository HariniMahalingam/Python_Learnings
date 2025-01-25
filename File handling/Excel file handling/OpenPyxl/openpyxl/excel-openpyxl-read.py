'''
openpyxl is an lib in python
used for file handling with excel workbooks.

various lib available for excel in python
 -pandas, openpyxl, xlrd, xlswriter, iornxl mostly used for excel file handling.


'''



#Steps
#1 pip install openpyxl

# import openpyxl module
import openpyxl

# Give the location of the file
path = "cars.xlsx"

# To open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path) #.loadworkbook() is used to open the excel workbook.

# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active # .active first_sheet of the excel workbook.

cell_obj = sheet_obj.cell(row=1, column=1) #.cell - to mention the pos of the cursor.

print(cell_obj.value)#print the cursor cell value.

print("printing only one cell")

#max_row, max_column is used to check the length of row and column in the excel

path = "cars.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

row = sheet_obj.max_row #return the total rows.
column = sheet_obj.max_column #return the total columns.
print("printing all the cell")
for i in range(1,row+1):
    for j in range(1,column+1):
        cursor = sheet_obj.cell(row=i,column=j)
        print('row-',i,' column-',j,' value-',cursor.value)

#reading using cell specific in excel
import openpyxl

# Give the location of the file
path = "cars.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

cell_obj = sheet_obj['A1': 'B6'] #if i give an random cell no's also it will execute, but value will be printed as null

for cell1, cell2 in cell_obj:
    print(cell1.value, cell2.value)






