import pandas as pd

seattle_restaurants = [
    ['Bakery Nouveau', 'French', 4.6],
    ['Pizzeria Credo', 'Italian', 4.6],
    ['Chan Seattle', 'Korean', 4.4],
    ['Tilikum Place Cafe', 'European', 4.6],
    ['Ba Bar Capitol Hill', 'Vietnamese', 4.5]
]
 
seattle_restaurants_df = pd.DataFrame(
    data=seattle_restaurants,
    columns=['Restaurant', 'Cuisine', 'Rating']
)
 
# Print DataFrame contents
seattle_restaurants_df

seattle_restaurants_df.to_excel(
    'seattle_restaurants.xlsx',
    # Don't save the auto-generated numeric index
    index=False
)



print("completed 1")

Employee = [
    ['Harini',23,'Data Scientist'],
    ['Thaarun',23,'SDE 1'],
    ['Bala',35,'SDE 3']
]
emp_df = pd.DataFrame(data=Employee,columns=['Name','Age','Role'])
emp_df.to_excel("Employee.xlsx",index=False)
print("Employee completed")