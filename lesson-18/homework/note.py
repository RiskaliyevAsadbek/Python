import pandas as pd

df = pd.read_csv("C:\\Users\\user\\Downloads\\tackoverflow_qa.csv")
print(df.head())

# 1 Find all questions that were created before 2014
filtered = df[df['creationdate'] < '2014-01-01']
print(filtered.head(10))

# 2 Find all questions with a score more than 50
filtered_score = df[df['score'] > 50]
print(filtered_score.head(10))

# 3 Find all questions with a score between 50 and 100
filtered_score2 = df[(df['score'] > 50) & (df['score'] < 100)]
print(filtered_score2.head(10))

# 4 Find all questions answered by Scott Boston
filtered_name = df[df['ans_name'] == 'Scott Boston']
print(filtered_name)

# 5 Find all questions answered by the following 5 users
filtered_name2 = df[(df['ans_name'].isin(['Scott Boston', 'Avaris', 'doug', 'Wes McKinney', 'Siva-Sg']))]
print(filtered_name2)

# 6 Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
df['creationdate'] = pd.to_datetime(df['creationdate'])
filtered2 = df[(df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31') & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)]
print(filtered2)

# 7 Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
filtered_view = df[(df['score'] > 5) & (df['score'] < 10) & (df['viewcount'] > 10000)]
print(filtered_view)

# 8 Find all questions that are not answered by Scott Boston
filterd_name3 = df[df['ans_name'] != 'Scot Boston']
print(filterd_name3)

# Homework 3
df2 = pd.read_csv("C:\\Users\\user\\Downloads\\titanic.csv")
print(df2.head())

# PassengerId: Id of every passenger.
# Survived: Indication whether passenger survived. 0 for yes and 1 for no.
# Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
# Name: Name of passenger.
# Sex: Gender of passenger.
# Age: Age of passenger in years.
# SibSp: Number of siblings or spouses aboard.
# Parch: Number of parents or children aboard.
# Ticket: Ticket number of passenger.
# Fare: Indicating the fare.
# Cabin: Cabin number of passenger.
# Embarked: Port of embarkation.

# 1 Select Female Passengers in Class 1 with Ages between 20 and 30: 
# Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
filt = df2[(df2['Sex'] == 'female') & (df2['Pclass'] == 1) & (df2['Age'] > 20) & (df2['Age'] < 30)]
print(filt)

# 2 Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
filt2 = df2[df2['Fare'].astype(float) > 100]
print(filt2)

# 3 Select Passengers Who Survived and Were Alone: 
# Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
filt3 = df2[(df2['Survived'].astype(float) == 0) & (df2['SibSp'] == 0) & (df2['Parch'] == 0)]
print(filt3)

# 4 Filter Passengers Embarked from 'C' and Paid More Than $50: 
# Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
filt4 = df2[(df2['Embarked'] == 'C') & (df2['Fare'].astype(float) > 50)]
print(filt4)

# 5 Select Passengers with Siblings or Spouses and Parents or Children: 
# Extract passengers who had both siblings or spouses aboard and parents or children aboard.
filt5 = df2[(df2['Parch'] == 1) & df2['SibSp'] == 1]
print(filt5)

# 6 Filter Passengers Aged 15 or Younger Who Didn't Survive: 
# Create a DataFrame with passengers aged 15 or younger who did not survive.
filt6 = df2[(df2['Age'] <= 15) & (df2['Survived'] == 0)]
print(filt6)

# 7 Select Passengers with Cabins and Fare Greater Than $200: 
# Extract passengers with known cabin numbers and a fare greater than $200.
filt7 = df2[(df2['Cabin'] != 'NaN') & (df2['Fare'] > 200)]
print(filt7)

# 8 Filter Passengers with Odd-Numbered Passenger IDs: 
# Create a DataFrame with passengers whose PassengerId is an odd number.
filt8 = df2[df2['PassengerId'] % 2 != 0]
print(filt8.head(10))  # in order to see the first 10 odd number passengerID

# 9 Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
filt9 = df2['Ticket'].value_counts()
filt9_2 = filt9[filt9 == 1].index
filt9_3 = df2[df2['Ticket'].isin(filt9_2)]
print(filt9_3)

# 10 Filter Passengers with 'Miss' in Their Name and Were in Class 1:
#  Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
filt10 = df2[(df2['Pclass'] == 1) & (df2['Sex'] == 'female') & (df2['Name'].str.contains('Miss'))]
print(filt10)
