# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    num = int(input('enter the number: '))
    res = num / 0
except ZeroDivisionError:
    print('you cannot divide by zero!')
finally:
    print('code executed successfully')

# 2 Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num_str = input('enter the number')
    num = int(num_str)
except ValueError:
    print('you entered invalid value, please enter valid value')
else:
    print('you entered valid value')
finally:
    print('the code executed successfully') 

# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open('new_txt') as file:
        print(file)
except FileNotFoundError:
    print('the file you enterd is not found')
else:
    print('we have found your file')    
finally:
    print('code executed successfully')

# 4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    num = input('enter the number')
    result = num / 8
except TypeError:
    print('you enterd invalid type of value')
else:
    print(f'your result is: {result}')  
finally:
    print('your code executed successfully')  

# 5 Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open("/root/protected_test.txt", "w") as file:
        file.write("Testing PermissionError")
except PermissionError:
    print("PermissionError: You do not have permission to write to this location.")
finally:
    print('your code executed')

# 6 Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
     fruit_list = ['apple', 'mango', 'kiwi']
     for i in fruit_list:
        print(i[7])                            
except IndexError:
    print('too short to access index 7')
else:
    print(i[7])
finally:
    print('your code executed successfully') 
    
# 7 Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.    
try:
   
    number = input("Enter a number: ")
    number = float(number)  
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("KeyboardInterrupt: Input was cancelled by the user.")

# 8 Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error. 
try:
    num = 98
    res = num / 0
except ArithmeticError:
    print('there is a arithematic error')
else:
    print(f'yor reslut is {res}')
finally:
    print('your code executed') 

# 9 Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.               
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("UnicodeDecodeError: Could not decode the file with UTF-8 encoding.")

# 10 Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
my_list = [1, 2, 3, 4, 5]
try:
    my_list.uppercase()   
except AttributeError:
    print("AttributeError: 'list' object has no attribute 'uppercase'.")
    
# File Input/Output Exercises    
# 1 Write a Python program to read an entire text file.
with open("C:\\Users\\user\\Documents\\my_txt.txt") as file:
   content = file.read()
   print(content)
# 2 Write a Python program to read first n lines of a file.
def read_first_n_lines(filename, n):
    with open(filename) as file:
        for l in range(n):
            line = file.readline()
    print(line)

read_first_n_lines("C:\\Users\\user\\Documents\\my_txt.txt", 3)

# 3 Write a Python program to append text to a file and display the text.
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'a') as file:
    file.write('\nwhat is your favorite fruit?')

with open("C:\\Users\\user\\Documents\\my_txt.txt", "r") as file:
    content = file.read()
    print(content)

# 4 Write a Python program to read last n lines of a file.
def read_last_n_lines(filename, n):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()   
            last_lines = lines[-n:]   
            for line in last_lines:
                print(line.strip())
    except FileNotFoundError:
        print("FileNotFoundError: The specified file does not exist.")

read_last_n_lines("C:\\Users\\user\\Documents\\my_txt.txt", 3)

# 5 Write a Python program to read a file line by line and store it into a list.
my_line_list = []
with open("C:\\Users\\user\\Documents\\my_txt.txt") as file:
    for line in file:
        my_line_list.append(line.strip())
print(my_line_list)

# 6 Write a Python program to read a file line by line and store it into a variable.
file_content = ''
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    for line in file:
        file_content += line

print(file_content)

# 7 Write a Python program to read a file line by line and store it into an array.
file_line_list = []
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    for line in file:
        file_line_list.append(line.strip())
print(file_line_list)

# 8 Write a Python program to find the longest words.
words = []
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    for line in file:
        line_list=line.split()
        for i in line_list:
            words.append(i)
            
words.sort(key= lambda a: len(a), reverse=True)     
print(f'the longest word is {words[0]}') 

# 9 Write a Python program to count the number of lines in a text file.
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    print(len(file.readlines()))

# 10 Write a Python program to count the frequency of words in a file.
my_dict = {}
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    for line in file:
        line_list = line.split()
        for i in line_list:
            my_dict[i] =  my_dict.get(i, 0) + 1  

print(my_dict)

# 11 Write a Python program to get the file size of a plain file.

# 1st option
import os
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    print(os.path.getsize("C:\\Users\\user\\Documents\\my_txt.txt"))

# 2nd option
with open("C:\\Users\\user\\Documents\\my_txt.txt", "rb") as file:  
    content = file.read()             
    size = len(content)              

print(f"File size: {size} bytes")   

# 12 Write a Python program to write a list to a file.
fruit_list = ["apple", "banana", "kiwi"]
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'a') as file:
    for item in fruit_list:
        file.write('\n'+ item)
    
# 13 Write a Python program to copy the contents of a file to another file.
with open("C:\\Users\\user\\Documents\\my_txt.txt", 'r') as file:
    content = file.read()

with open("C:\\Users\\user\\Documents\\txt2.txt", 'w') as second_file:
    second_file.write(content)   

print('file copied to second_file successfully')     
    
# 14 Write a Python program to combine each line from the first file with the corresponding line in the second file.
file1_path = "C:\\Users\\user\\Documents\\my_txt.txt"
file2_path = "C:\\Users\\user\\Documents\\txt2.txt"

with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())       


# 15 Write a Python program to read a random line from a file.
import random

with open("C:\\Users\\user\\Documents\\my_txt.txt", "r") as file:
    lines = file.readlines()
    print(random.choice(lines).strip())

# 16 Write a Python program to assess if a file is closed or not.
file_path = "C:\\Users\\user\\Documents\\my_txt.txt"

with open(file_path, "r") as f:
    print("Inside 'with' block - is file closed?", f.closed) 

print("Outside 'with' block - is file closed?", f.closed)

# 17 Write a Python program to remove newline characters from a file.
file_path = "C:\\Users\\user\\Documents\\my_txt.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
cleaned_lines = [line.strip() for line in lines]

print(cleaned_lines)    

# 18 Write a Python program that takes a text file as input and returns the number of words in a given text file.
file_path = "C:\\Users\\user\\Documents\\my_txt.txt"

with open(file_path, "r") as file:
    text = file.read()             
    words = text.split()           
    print("Number of words:", len(words))
         
# 19 Write a Python program to extract characters from various text files and put them into a list.
file_paths = [
    "C:\\Users\\user\\Documents\\my_txt.txt",
   "C:\\Users\\user\\Documents\\txt2.txt"
]

characters = []

for path in file_paths:
    with open(path, "r") as file:
        content = file.read()          
        for char in content:          
            characters.append(char)

print(characters)

# 20 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

for i in range(65, 91):  
    letter = chr(i)
    filename = f"{letter}.txt"
    with open("C:\\Users\\user\\Documents\\my_txt.txt", "a") as file:
        file.write(f"This is file {filename}\n")

 # 21 Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input("Enter the number of letters per line: "))

with open("C:\\Users\\user\\Documents\\txt2.txt", "w") as file:
    for i in range(0, len(alphabet), n):
        line = alphabet[i:i+n]  
        file.write(line + "\n")  

print("File 'alphabet.txt' created successfully!")
        


         
        
        
     




    
