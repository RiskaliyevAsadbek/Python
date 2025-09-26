# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, 
# shift the underscore placement to the next character. 
# No underscore should be added at the end.

used_chars = ['a', 'e', 'i', 'u', 'o']
index = 2
my_txt = 'abcabcabcdeabcdefabcdefgyy'

while index < len(my_txt) - 1:
    if my_txt[index] not in used_chars:
        used_chars.append(my_txt[index])
        my_txt = my_txt[:index + 1] + '_' + my_txt[index +1:]
        index += 4
        
    else:
        index += 1

print(my_txt)

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

# Example Input
# 5
# Example Output
# 0
# 1
# 4
# 9
# 16
# Input Format
# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20
# Output Format
# Print n lines, one corresponding to each i^2 where 0 <= i < n.

# 1st option
number = int(input('enter the number: '))
for i in range(0,number):
      if 1 <= number <= 20:
             print(i * i)

# 2nd option
number = int(input('enter the number: '))
for i in range(0,number):
      if 1 <= number <= 20:
             print(i ** 2)
      
# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop
number = 1
while number < 11:
      print(number)
      number += 1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5  
n = int(input('enter the number: '))  
for i in range(1, n + 1):     
    for j in range(1, i + 1):     
        print(j, end=" ")         
    print()                       

# Exercise 3: Calculate sum of all numbers from 1 to a given number

# 1st option with while loop
N = int(input('enter the number: '))
start = 1
my_total = 0
while start <= N:
      my_total +=start
      start += 1
print(f'sum is: {my_total}') 

# 2nd option with for loop
N = int(input('enter the number: '))
my_total = 0
for i in range(1,N+1):
      my_total +=i
print(f'sum is: {my_total}')

# Exercise 4: Print multiplication table of a given number

# 1st option with while loop:
Number = int(input('enter the number: '))
start = 1
while start <= 10:
      print(start * Number)
      start +=1

# 2nd option with for loop:
Number = int(input('enter the number: '))
for i in range(1, 11):
      print(i * Number)

# Exercise 5: Display numbers from a list using a loop

# 1st option with  for loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
      if i % 5 ==0:
            if i <= 150:
                   print(i)
      if i > 500:
            break

# 2nd option with while loop
numbers = [12, 75, 150, 180, 145, 525, 50]
count = 0
while  count < len(numbers):
      if numbers[count] % 5 == 0:
            if numbers[count] <= 150:
                  print(numbers[count])
      if numbers[count] > 500:
            break            
      count +=1 

# Exercise 6: Count the total number of digits in a number 

# 1st option with for loop   
NUMBER = input('enter the number: ')
cnt = 0
for i in NUMBER:
      cnt +=i.count(i)          
print(cnt)             

# 2nd option with while loop   
NUMBER = input('enter the number: ')
cnt = 0
while cnt < len(NUMBER):
      cnt +=1
print(cnt)

# Exercise 7: Print reverse number pattern

# 1st option with for loop
rows = int(input('enter the number'))
for i in range(rows, 0, -1):
    line = ""                     
    for j in range(i, 0, -1):
        line += str(j) + " "       
    print(line) 

# 2nd option with while loop
rows = int(input('enter the number: '))
i = rows
while i > 0:
    line = ""                
    j = i
    while j > 0:
        line += str(j) + " " 
        j -= 1
    print(line)
    i -= 1          

# Exercise 8: Print list in reverse order using a loop

# 1st option
list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
      print(i)

# 2nd option
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) -1, -1,-1):
      print(list1[i])      

# 3rd option
list1 = [10, 20, 30, 40, 50]
lenght = len(list1) - 1
while lenght >=0:
      print(list1[lenght])
      lenght -=1

# 4th option
list1 = [10, 20, 30, 40, 50]
list1.reverse()
cnt = 0
while cnt < len(list1):
      print(list1[cnt])
      cnt +=1        

# Exercise 9: Display numbers from -10 to -1 using a for loop 

# 1st option with for loop
n = -1
for i in range(-10, n+1):
      print(i)  

# 2nd option with while loop
n = -10
while n <= -1:
      print(n)
      n += 1          

# Exercise 10: Display message “Done” after successful loop execution 

# 1st option with for loop
num = int(input('enter the number: '))
for i in range(1,num + 1):
      print(i)
print('DONE!')      

# 2nd option with while loop
num = int(input('enter the number: '))
coun = 1
while coun <= num:
      print(coun)
      coun +=1
print('DONE!')

# Exercise 11: Print all prime numbers within a range

# 1st option with for loop
num_start = int(input('enter starting number of the range: '))
num_end = int(input('enter ending number of the range: '))
for i in range(num_start, num_end + 1):
      for num in range(2, i):
            if i % num == 0:
                  break
      else:
            print(i)
            
# 2nd option with while loop
num_start = int(input('enter starting number of the range: '))
num_end = int(input('enter ending number of the range: '))
while num_start <= num_end:
      num_start +=1
      num = 2
      while num in range(num,num_start):
            if num_start % num == 0:
                  break
            num +=1
      else:
            print(num_start)      

# Exercise 12: Display Fibonacci series up to 10 terms

# 1st option with for loop
term = 10
a,b = 0,1
for i in range(term):
      print(a)
      a ,b = b, a+b
     
# 2nd option with while loop
term = 10
a,b = 0,1
coun = 0
while coun < term:
      print(a)
      a,b = b, a+b
      coun +=1    

# Exercise 13: Find the factorial of a given number

# 1st option with for loop
integer = int(input('enter the number: '))
factorial = 1
for i in range(1,integer +1):
      factorial *=i
print(f'{integer}! = {factorial}')

# 2nd option with while loop
integer = int(input('enter the number: '))
factorial = 1
cnt = 1
while cnt <= integer:
     factorial *= cnt
     cnt +=1 
print(f'{integer}! = {factorial}')

# 4. Return Uncommon Elements of Lists
list1 = list(map(int, input('enter the numbers: ').split(',')))
list2 = list(map(int, input('enter the numbers: ').split(',')))
result = []
for i in list1:
      if i not in list2:
            result.append(i)
for j in list2:
      if j not in list1:
            result.append(j)
print(result)   


# 2nd option
raw_input1 = input("Enter numbers for list 1: ").strip()
if ',' in raw_input1:       
    list1 = list(map(int, raw_input1.split(',')))
else:                        
    list1 = [int(x) for x in raw_input1]


raw_input2 = input("Enter numbers for list 2: ").strip()
if ',' in raw_input2:       
    list2 = list(map(int, raw_input2.split(',')))
else:                        
    list2 = [int(x) for x in raw_input2]


result = []
for i in list1:
    if i not in list2:
        result.append(i)
for j in list2:
    if j not in list1:
        result.append(j)

print("Uncommon elements:", result)

