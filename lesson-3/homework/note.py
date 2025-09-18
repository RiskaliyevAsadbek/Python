# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

fruit = ['lemon', 'pineapple', 'kiwi', 'orange', 'passion fruit']
print(fruit[2])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

# 1st option
number_l1 = [1, 2, 3, 4, 5]
number_l2 = [6, 7, 8, 9, 10]
combined = number_l1 + number_l2
print(combined)

#2nd option
number_l1 = [1, 2, 3, 4, 5]
number_l2 = [6, 7, 8, 9, 10]
number_l1 += number_l2
print(number_l1)

#3rd option
number_l1 = [1, 2, 3, 4, 5]
number_l2 = [6, 7, 8, 9, 10]
number_l1.extend(number_l2)
print(number_l1)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_num = numbers[0]
l = len(numbers) // 2
middle_num = numbers[l]
last_num = numbers[-1]
stored = []
stored.append(first_num)
stored.append(middle_num)
stored.append(last_num)
print(stored)

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

movie_list = ['the fault of our stars', 'five feet apart', 'rosemary and thyme', 'wednesday', 'devil wears prada']
movie_tuple = tuple(movie_list)
print(type(movie_tuple))

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

city_list = ['London', 'Paris', 'Ottawa', 'Rome', 'Seoul']
check_ = city_list.index('Paris')
print(city_list[check_])

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

num = [1, 2, 3, 4, 5]
dublicate = num.copy()
comb = num + dublicate
print(comb)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

#1st option
num = [1, 2, 3, 4, 5]
first = num.pop(0)      
last = num.pop(-1)     
num.insert(0, last)     
num.append(first) 
print(num)  

#2nd option
num = [1, 2, 3, 4, 5]
temp = num[0]
num[0] = num[-1]
num[-1] = temp
print(num)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

num_tuple = (1, 2, 3 , 4, 5, 6, 7, 8, 9, 10)
print(num_tuple[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

color_list = ['blue', 'red', 'yellow', 'purple', 'blue', 'blue', 'purple']
print(color_list.count('blue'))

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animal_tuple = ('lion', 'snake', 'tiger', 'elephant', 'wolf')
print(animal_tuple.index('lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

num_tuple1 = (1, 2, 3, 4, 5)
num_tuple2 = (6, 7, 8, 9,)
num_tuple1 += num_tuple2
print(num_tuple1)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
list = [1, 2, 3, 4, 5]
tuple = (1, 23, 4, 5, 54)
print('the lenght of list is; ', len(list))
print('the lenght of tuple is; ', len(tuple))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

tuple = (1, 23, 4, 5, 54)
tuple_to_list = list(tuple)
print(type(tuple_to_list))

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

# 1st option
tup_num = (1, 2, 34, 68, 98)
max_ = max(tup_num)
min_ = min(tup_num)
print('the maximum number is ', max_)
print('the minimum number is ', min_)

# 2nd option 
tup_num = (1, 2, 34, 68, 98)
sorted = sorted(tup_num)
print(f" the maximum number is {sorted[-1]}, the minimum number is {sorted[0]} ")

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

tup_words = ('bye', 'apple', 'book', 'pen', 'crayon')
print(tup_words[: : -1])
