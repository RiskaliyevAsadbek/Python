# Homework 1:

# import pandas as pd

# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame
import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)  # df- I created DataFrame
print(df)

#1
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
#2
print(df.head(3))
#3
mean_age = df['age'].mean()
print(mean_age)
#4
print(df[['first_name', 'City']])
#5
df['Salary'] = np.random.randint(5000,10000,size=len(df))
print(df)
#6
print(df.describe())

# Homework 2:

# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500
# Calculate and display the maximum sales and expenses.
# Calculate and display the minimum sales and expenses.
# Calculate and display the average sales and expenses.

import pandas as pd
data2 = {'Month':['Jan', 'Feb', 'Mar', 'Apr'], 'Sales':[5000,6000,7500,8000], 'Expenses': [3000, 3500, 4000, 4500]}
df2 = pd.DataFrame(data2)
print(df2)
#1
maximum_sale = df2['Sales'].max()
maximum_expenses = df2['Expenses'].max()
print(maximum_sale)
print(maximum_expenses)

#2
minimum_sales = df2['Sales'].min()
minimum_expenses = df2['Expenses'].min()
print(minimum_sales)
print(minimum_expenses)

#3
average_sales = df2['Sales'].mean()
average_expenses = df2['Expenses'].mean()
print(average_sales)
print(average_expenses)

# Homework 3:

# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
# Calculate and display the maximum expense for each category.
# Calculate and display the minimum expense for each category.
# Calculate and display the average expense for each category.
# In this task, use .set_index method to make Category column as index.

# Try this code, learn it and use it in the task.
# expenses.set_index('Category')

import pandas as pd
data3 ={'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 'January': [1200, 200, 300, 150], 'February': [1300, 220, 320, 160], 'March': [1400, 240, 330, 170], 'April': [1500, 250, 350, 180]}
df3 = pd.DataFrame(data3)
print(df3)

# 1 max expense for each category
df3['Max_expenses'] = df3[['January', 'February', 'March', 'April']].max(axis=1)
print(df3[['Category', 'Max_expenses']])

# 2
df3['Min_expenses'] = df3[['January', 'February', 'March', 'April']].min(axis=1)
print(df3[['Category', 'Min_expenses']])

# 3
df3['Average_expenses'] = df3[['January', 'February', 'March', 'April']].mean(axis=1)
print(df3[['Category', 'Average_expenses']])

import pandas as pd
data3 ={'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 'January': [1200, 200, 300, 150], 'February': [1300, 220, 320, 160], 'March': [1400, 240, 330, 170], 'April': [1500, 250, 350, 180]}
Expenses = pd.DataFrame(data3)
Expenses = Expenses.set_index('Category')
print(Expenses)
Expenses['Max_expenses'] = Expenses.max(axis=1)
print(Expenses)
Expenses['Min_expenses'] = Expenses.min(axis=1)
print(Expenses)
Expenses['Average_expenses'] = Expenses.mean(axis=1)
print(Expenses)
