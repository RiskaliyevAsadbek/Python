# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
Original_List = [12.23, 13.32, 100, 36.32]
import numpy as np
arr = np.array(Original_List, ndmin=1)
print('1D array acreated', arr)

# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np

matrix_0 = np.zeros(10)
matrix_0[5] = 11
print(matrix_0)

# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np
matrix_4 = np.arange(12, 38)
print(matrix_4)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.

# Sample output:

# Original array [1, 2, 3, 4]

import numpy as np
array = np.array([1, 2, 3, 4])
converted = array.astype(float)
print(converted.dtype) 

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

# Expected Output:

# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

# Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]
import numpy as np

# Celsius values
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])

# Convert Celsius → Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convert Fahrenheit → Celsius (optional check)
celsius_converted_back = (fahrenheit - 32) * 5/9

print("Values in Celsius degrees:", np.round(celsius, 2))
print("Values in Fahrenheit degrees:", np.round(fahrenheit, 2))
print("\nConverted back to Celsius (for verification):", np.round(celsius_converted_back, 2))

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.

# Expected Output:

# Original array: [10, 20, 30]

# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

import numpy as np

arr = np.array([10, 20, 30])
print("Original array:", arr)

values_to_append = [40, 50, 60, 70, 80, 90]

new_arr = np.append(arr, values_to_append)

print("\nAfter appending values to the end of the array:", new_arr)

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
import numpy as  np
data = np.random.randint(0,10,10)
mean = data.mean()
median = np.median(data)
std_deviation = np.std(data)
print('The mean of array is: ', mean)
print('The median of array is: ', median)
print('The standard deviation of array is: ', std_deviation)

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as  np
data2 = np.random.randint(0,100,100).reshape(10,10)
maximum = data2.max()
minimum = data2.min()
print('The maximum value is: ',maximum)
print('The minimum value is: ',minimum)

# 10
# Create a 3x3x3 array with random values.
import numpy as  np
data3 = np.random.randint(0,100,27).reshape(3,3,3)
print(data3)

data4 = np.random.random((3,3,3))
print('3x3x3 array with float values',data4)




