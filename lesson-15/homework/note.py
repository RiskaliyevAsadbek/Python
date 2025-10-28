# 1 Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3 
with sqlite3.connect("Homework15.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)
print('Roster table created')    

# 2 Populate your new table with the following values:

# Name	Species	Age
# Benjamin Sisko	Human	40
# Jadzia Dax	Trill	300
# Kira Nerys	Bajoran	29

Values = [('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]
with sqlite3.connect("Homework15.db") as conn:
    cursor = conn.cursor()
    cursor.executemany("""
      INSERT INTO Roster (Name, Species, Age) VALUES(?,?,?)
    """, Values)
conn.commit()    
print('Data inserted')

# 3 Update the Name of Jadzia Dax to be Ezri Dax
with sqlite3.connect("Homework15.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Roster
        SET Name = ?
        WHERE Name = ?
    """, ('Ezri Dax', 'Jadzia Dax'))
conn.commit()
print('Name Updated')    

# 4 Display the Name and Age of everyone in the table classified as Bajoran.   
with sqlite3.connect("Homework15.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''
     SELECT Name, Age FROM Roster
     WHERE Species = 'Bajoran'              
''')
print('Task is done')

results = cursor.fetchall()  
    
print(" Bajoran crew members:")
for name, age in results:
        print(f"Name: {name}, Age: {age}")



