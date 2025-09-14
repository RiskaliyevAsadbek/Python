
# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input('write down your name ')
birth_year = int(input('enter your year of birth '))
from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year
print(f'hello {name}.Your age is {age}')

# 2. Extract Car Names
# Extract car names from the following text:
txt1 = 'LMaasleitbtui'
first_char = txt1[-3]
second_char = txt1[6]
third_char = txt1[4]
fourth_char = txt1[5]
fifth_char = txt1[2]
print(''.join([first_char, second_char,third_char,fourth_char,fifth_char]))

# 3. Extract Car Names
# Extract car names from the following text:

txt = 'MsaatmiazD'
first_let = txt[0]
second_let = txt[2]
third_let = txt[-2]
fourth_let = txt[-1]
fifth_let = txt[2]
print(''.join([first_let, second_let, third_let, fourth_let.lower(), fifth_let]))

# 4. Extract Residence Area
# Extract the residence area from the following text:

txt2 = "I'am John. I am from London"
start = txt2.index('from')
residence = txt2[start + len('from ') : ]
print(residence)

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

string = input('enter your string')
reverse = string[::-1]
print('your reversed string is: ', reverse)

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

word = input('write down your word')
number_of_a = word.count('a')
number_of_e = word.count('e')
number_of_i = word.count('i')
number_of_o = word.count('o')
number_of_u = word.count('u')
number_of_y = word.count('y')

number_of_A = word.count('A')
number_of_E = word.count('E')
number_of_I = word.count('I')
number_of_O = word.count('O')
number_of_U = word.count('U')
number_of_Y = word.count('Y')

number_of_vowels = number_of_A + number_of_E + number_of_I + number_of_O + number_of_U + number_of_Y + number_of_a + number_of_e + number_of_i + number_of_o + number_of_u + number_of_y
print(number_of_vowels)

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

number = list(input('enter your numbers').split(' '))
maximum_value = max(number)
print(maximum_value)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

text = input('enter the word ').lower()
polindrome_check = text[::-1]
if text == polindrome_check :
  print('your word is polindrone')
else :
  print('your word is not polindrome')

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input('Please enter your email ')
position_of = email.index('@')
domain = email[position_of + 1 :]
print(domain)

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
