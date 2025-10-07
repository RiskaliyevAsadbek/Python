# 1 Create your own virtual environment and install some python packages.
PS C:\Users\user\Documents\python lessons f35\python lesson 11> pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.34.0-py3-none-any.whl.metadata (4.6 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)
  Downloading distlib-0.4.0-py2.py3-none-any.whl.metadata (5.2 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv)
  Downloading filelock-3.19.1-py3-none-any.whl.metadata (2.1 kB)
Collecting platformdirs<5,>=3.9.1 (from virtualenv)
  Downloading platformdirs-4.4.0-py3-none-any.whl.metadata (12 kB)
Downloading virtualenv-20.34.0-py3-none-any.whl (6.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 15.3 MB/s  0:00:00
Downloading distlib-0.4.0-py2.py3-none-any.whl (469 kB)
Downloading filelock-3.19.1-py3-none-any.whl (15 kB)
Downloading platformdirs-4.4.0-py3-none-any.whl (18 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.4.0 filelock-3.19.1 platformdirs-4.4.0 virtualenv-20.34.0                                                                   
PS C:\Users\user\Documents\python lessons f35\python lesson 11> pip list
Package      Version
------------ -------
distlib      0.4.0
filelock     3.19.1
pip          25.2
platformdirs 4.4.0
virtualenv   20.34.0
PS C:\Users\user\Documents\python lessons f35\python lesson 11> virtualenv my_env
created virtual environment CPython3.12.9.final.0-64 in 8464ms
  creator CPython3Windows(dest=C:\Users\user\Documents\python lessons f35\python lesson 11\my_env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C:\Users\user\AppData\Local\pypa\virtualenv)
    added seed packages: pip==25.2
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
PS C:\Users\user\Documents\python lessons f35\python lesson 11> Set-ExecutionPolicy Unrestricted -Scope Process
PS C:\Users\user\Documents\python lessons f35\python lesson 11> .\my_env\Scripts\Activate
(my_env) PS C:\Users\user\Documents\python lessons f35\python lesson 11> 
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. 
# (All functions accept two arguments in this task)
C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\math_operations.py # math_operations module is created
def add(a: int, b: int):
    return f'{a} + {b} = {a+b}'
def substract(a: int, b: int):
    return f'{a} - {b} = {a-b}'
def multiply(a: int, b: int):
    return f'{a} x {b} = {a*b}'
def divide(a: int, b: int):
    return f'{a} / {b} = {a/b}'
# Create string_utils.py module. Define reverse_string and count_vowels functions in it. moduleas are created!
# (All functions accept one argument in this task)
def reverse_string(any_str: str):
    return any_str[ : : -1]

def count_vowels(any_string: str):
    vowels = ['a', 'e', 'o', 'i', 'u']
    result = 0
    for i in any_string:
        if i.lower() in vowels:
            result +=1
    return result  
  # Create custom packages: Create geometry package.
  C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\geometry  #package geometry created
# Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\geometry\circle.py  #module is created
def calculate_area(radius: int):
    import math
    return math.pi * (radius ** 2)

def calculate_circumference(radius: int):
    import math
    return 2 * math.pi * radius

#Create file_operations package.
C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\file_operations  # package file_operations is created
#Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).
C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\file_operations\file_reader.py  # module file_reader.py is created
def read_file(file_path: str):
      try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
      except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
      except Exception as e:
        return f"An error occurred while reading the file: {e}"

C:\Users\user\Documents\python lessons f35\python lesson 11\my_env\file_operations\file_writer.py  #module file_writer.py is created
def write_file(file_path: str, content: str):
     try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f" Successfully wrote to '{file_path}'."
     except Exception as e:
        return f" An error occurred while writing to the file: {e}"

