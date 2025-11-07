# DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
print(df1)
# Exercise 1: Calculate the average grade for each student.
# O'rtacha bahoni hisoblash (Math, English, Science ustunlari bo'yicha)
df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1)

# Exercise 2: Find the student with the highest average grade.
filter = df1['Average_Grade'].max()
top_student = df1[df1['Average_Grade'] == filter]
print(top_student)
# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1)
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
import matplotlib.pyplot as plt
subject_avg = df1[['Math', 'English', 'Science']].mean(axis=1)
# subjects = subject_avg.keys().to_list()
# subject_values = subject_avg.values
plt.bar(subject_avg.index, subject_avg.values)
plt.title("Average Grades per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.show()

# DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
# Exercise 1: Calculate the total sales for each product.
df2['total_sale'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
print(df2)
# Exercise 2: Find the date with the highest total sales.
sort = df2.sort_values('total_sale', ascending=False).head(1)
print(sort)
# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2['Date'] = pd.to_datetime(df2['Date'])
df2['A_change_%'] = df2['Product_A'].pct_change() * 100
df2['B_change_%'] = df2['Product_B'].pct_change() * 100
df2['C_change_%'] = df2['Product_C'].pct_change() * 100
print(df2)
# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product C')
plt.title("Sales Trends of Products Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.legend()

plt.show()

# DataFrame 3: Employee Information
import pandas as pd
import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
# Exercise 1: Calculate the average salary for each department.
filtered = df3.groupby('Department')['Salary'].mean()
print(filtered)
merge = pd.merge(df3, filtered, on='Department')
print(merge)
# Exercise 2: Find the employee with the most experience.
filtered1 = df3['Experience (Years)'].max()
top_employee = df3[df3['Experience (Years)'] == filtered1]
print(top_employee)
# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print(df3)
# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
dept_counts = df3['Department'].value_counts()
print(dept_counts)
plt.bar(dept_counts.index, dept_counts.values, color='skyblue')

plt.title("Distribution of Employees Across Departments")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()

# DataFrame 4: Customer Orders
import pandas as pd
import matplotlib.pyplot as plt
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
# Exercise 1: Calculate the total revenue from all orders.
totol_revenue = df4['Total_Price'].sum()
print(totol_revenue)

# Exercise 2: Find the most ordered product.
max_quantity = df4['Quantity'].max()
most_ordered_productm = df4[df4['Quantity'] == max_quantity]
print(most_ordered_productm)
# Exercise 3: Calculate the average quantity of products ordered.
avg_quantity = df4['Quantity'].mean()
print(avg_quantity)
# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Product")
plt.show()
