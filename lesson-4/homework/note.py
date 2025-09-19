
# Dictionary Exercises
# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

# 1st option
my_dictionary = {'ID':100, 'Age': 24, 'Experience': 5, 'Experience in a sphere of bank ': 4}
values = my_dictionary.values()
sorted_asc = sorted(values)
sorted_desc = sorted(values, reverse= True)
print(f'the value which is sorted in ascending order is {sorted_asc}, in descending order is {sorted_desc}')

# 2nd option
my_dictionary = {'ID':100, 'Age': 24, 'Experience': 5, 'Experience in a sphere of bank ': 4}
sorted_asc2 = dict(sorted(my_dictionary.items(), key=lambda item: item[1]))
sorted_desc2 = dict(sorted(my_dictionary.items(), key=lambda item: item[1], reverse=True))
print(f'the value which is sorted in ascending order is {sorted_asc2}, in descending order is {sorted_desc2}')

# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.

# 1st option
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 2nd option
my_dict = {0: 10, 1: 20}
my_dict.update([(2, 30)])
print(my_dict)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# 1st option
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(f"the merged dictionaries: {dic1}")

# 2nd option
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated = dic1 | dic2 | dic3
print(f" the merged dictionaries: {concatenated}")

# 3rd option 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {** dic1, ** dic2, ** dic3}
print(f'the merged dictianaries: {merged}')

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x), (n = 5)

n = 5
squares_dict = dict(map(lambda x: (x, x * x), range(1, n + 1)))
print(f"Dictionary with squares: {squares_dict}")

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

n = 15
squares_dict2 = dict(map(lambda x: (x, x * x), range(1, n + 1)))
print(f'Dictionary with squares(1 to 15): {squares_dict2}')

# Set Exercises
# 1. Create a Set

# 1st option
my_set = {1, 2, 3, 4, 5}
print(type(my_set))

# 2nd option
my_set2 = set()    #empty set
print(type(my_set2))

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.
my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
for item in my_city_set:
   print(f'the item of my set :{item}')

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
print(f'the original set: {my_city_set}')
my_city_set.add('Chiang Mai')
print(f' Add a single member by using add(): {my_city_set}')
my_city_set.update(['Singapore', 'Vancouver', 'Copenhagen'])
print(f'adding multiple members by using update(): {my_city_set}')

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

# 1st option with remove()
my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
my_city_set.remove('Rome')
print(my_city_set)

# 2nd option with discard()
my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
my_city_set.discard('Phuket')
print(my_city_set)

# 3rd option with pop()
my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
print(my_city_set.pop())
print(my_city_set)

# 4th option with clear() but it returns empty set
my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
my_city_set.clear()  # clear() returns empty set
print(my_city_set)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.

my_city_set = {'Seoul', 'Tokio', 'Paris', 'Rome', 'London', 'Prague', 'Phuket', 'Beijing'}
print(f'original set: {my_city_set}')
item = 'Tokio'
my_city_set.discard(item)
print(f'after removing the item {item} : {my_city_set}')
