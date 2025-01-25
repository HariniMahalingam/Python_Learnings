import csv

#reading an csv file
with open("read_csv.csv", mode='r') as read_file:
    csv_file= csv.reader(read_file) #reader method is used read the file
    for i in csv_file:
        print(i)

# writing_an_csv_file
company_list = [
    ['Expeditors','Logistics','Chennai'],
    ['Paypal','Finance','Chennai'],
    ['Walmart','E-commerce','Bangalore'],
    ['Amazon','E-commerce','Bangalore']
]
fields = ['Company_name','Domain','Location']
file_name= "list_of_companies.csv"

with open(file_name,'w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(fields)
    csv_writer.writerows(company_list)
print("Write() in CSV file")

# my data rows as dictionary objects
# dictionary values will only be inserted into the rows.
# it'll correctly map the headers as key and store respective values to that col.
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "university_records_using_dict.csv"

# writing to csv file
# opening the file in write mode.
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)

print("completed writing")


