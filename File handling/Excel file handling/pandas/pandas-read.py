'''
excel handling, using pandas
pandas underlying concept of read/write excel sheets are based on openpyxl concepts
read_excel() method used to read an excel.

'''


# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('cars.xlsx')

print(dataframe1)
print("")

#reading specific cols
require_cols = [0, 3]

# only read specific columns from an excel file
required_df = pd.read_excel('SampleWork.xlsx', usecols = require_cols)

print(required_df)
print("")

#na_values will update that particular cell as NAN for null/not applicable purpose.
dataframe = pd.read_excel('SampleWork.xlsx', na_values = "not available", sheet_name = 2)

print(dataframe)
print("")

# read 2nd sheet of an excel file
dataframe2 = pd.read_excel('cars.xlsx', sheet_name = 1)

print(dataframe2)
print(dataframe2.columns)

print("")
print("reading multiple sheets")

#reading multiple sheets
df = pd.read_excel('cars.xlsx', na_values = "Missing",sheet_name =[0, 1])

print(df)

print("")
print("reading all the sheets")
# read all sheets together.
all_sheets_df = pd.read_excel('cars.xlsx', na_values = "Missing",sheet_name = None)
print(all_sheets_df)

emp_read=pd.read_excel("Employee.xlsx")
print(emp_read)