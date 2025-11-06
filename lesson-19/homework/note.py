# Homework Assignment 1: Analyzing Sales Data
# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

# Date: Date of the sale.
# Product: Name of the product sold.
# Category: Category to which the product belongs.
# Quantity: Number of units sold.
# Price: Price per unit.
# Tasks:
# 1 Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
import pandas as pd

df = pd.read_csv("C:\\Users\\user\\Downloads\\sales_data.csv")
print(df)

filt1 = df.groupby('Category').agg({'Quantity': ['sum', 'max'], 'Price': ['mean']})
print(filt1)

# 2 Identify the top-selling product in each category based on the total quantity sold.
filt2 = df.groupby(['Category', 'Product'], as_index=False)['Quantity'].sum()
sorting = filt2.sort_values(['Category','Quantity'], ascending=[True,False]).groupby('Category').head(1)
print(sorting)

# 3 Find the date on which the highest total sales (quantity * price) occurred.
df['Total Sales'] = df['Quantity'] * df['Price']
filt3 = df.groupby('Date')['Total Sales'].sum()
filt3_2 = filt3.loc[filt3.idxmax()]
print("Highest total sales:", filt3_2)
print("Date:", filt3.idxmax())

# Homework Assignment 2: Examining Customer Orders

# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1 Group the data by CustomerID and filter out customers who have made less than 20 orders.
df2 = pd.read_csv("C:\\Users\\user\\Downloads\\customer_orders.csv")
print(df2)

filt4 = df2.groupby('CustomerID').filter(lambda x: len(x) < 20)
print(filt4)

# 2 Identify customers who have ordered products with an average price per unit greater than $120.
filt5 = df2.groupby('Product').filter(lambda y : y['Price'].mean() > 120)
print(filt5)

# 3 Find the total quantity and total price for each product ordered, 
# and filter out products that have a total quantity less than 5 units.
df2['TotalSales'] = df2['Quantity'] * df2['Price']
filt6 = df2.groupby('Product', as_index=False).agg({
    'Quantity': 'sum',
    'TotalSales': 'sum'
})
filt6 = filt6[filt6['Quantity'] < 5]

print(filt6)

# Homework Assignment 3: Population Salary Analysis

# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.
import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\\Users\\user\\Downloads\\population (1).db")

population_df = pd.read_sql("SELECT * FROM population", conn)

conn.close()  
print(population_df.head())

salary_bands = pd.read_excel("C:\\Users\\user\\Downloads\\population_salary_analysis.xlsx")
print(salary_bands)
salary_bands[['Min', 'Max']] = salary_bands['Salary Band'].str.split('-', expand=True)
salary_bands['Min'] = salary_bands['Min']
salary_bands['Max'] = salary_bands['Max']

def assign_category(salary):
    for _, row in salary_bands.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Category']
    return 'Unknown'

population_df['Salary_Category'] = population_df['salary'].apply(assign_category)

overall_stats = population_df.groupby('Salary_Category').agg(
    Population=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

total_population = population_df.shape[0]
overall_stats['Percentage'] = (overall_stats['Population'] / total_population) * 100

print("Overall Salary Category Stats:")
print(overall_stats)

state_stats = population_df.groupby(['State', 'Salary_Category']).agg(
    Population=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

state_population = population_df.groupby('state')['salary'].count().reset_index().rename(columns={'Salary':'State_Total'})

state_stats = state_stats.merge(state_population, on='state')
state_stats['Percentage'] = (state_stats['Population'] / state_stats['State_Total']) * 100
state_stats.drop(columns=['State_Total'], inplace=True)

print("\nSalary Category Stats by State:")
print(state_stats)
