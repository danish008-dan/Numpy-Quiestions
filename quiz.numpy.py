# NumPy Exercises (1 - 10)

import numpy as np
import matplotlib.pyplot as plt


# Exercise 1: Create a 4X2 integer array and print its attributes
print("Exercise 1:")
array1 = np.arange(8).reshape(4, 2)   # create 4x2 array
print("Array:\n", array1)
print("Shape:", array1.shape)
print("Dimensions:", array1.ndim)
print("Item size:", array1.itemsize)
print("Data type:", array1.dtype)
print("Size:", array1.size)
print("Type:", type(array1))
print("-" * 40)



# Exercise 2: Create a 5X2 integer array from a range between 100 to 200
# with step 10
print("Exercise 2:")
array2 = np.arange(100, 200, 10).reshape(5, 2)
print("Array:\n", array2)
print("-" * 40)



# Exercise 3: Take the third column from all rows
print("Exercise 3:")
sampleArray3 = np.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])
print("Original Array:\n", sampleArray3)
third_col = sampleArray3[:, 2]
print("Third column from all rows:", third_col)
print("-" * 40)



# Exercise 4: Return array of odd rows and even columns
print("Exercise 4:")
sampleArray4 = np.array([
    [3, 6, 9, 12],
    [15, 18, 21, 24],
    [27, 30, 33, 36],
    [39, 42, 45, 48],
    [51, 54, 57, 60]
])
print("Original Array:\n", sampleArray4)
result4 = sampleArray4[::2, 1::2]   # odd rows (0,2,4...) & even cols (1,3,...)
print("Odd rows & Even cols:\n", result4)
print("-" * 40)



# Exercise 5: Add two arrays and then square the result
print("Exercise 5:")
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 11]])
print("Array 1:\n", arrayOne)
print("Array 2:\n", arrayTwo)
result5 = arrayOne + arrayTwo
print("Sum of arrays:\n", result5)
result5_square = np.square(result5)
print("Square of result array:\n", result5_square)
print("-" * 40)



# Exercise 6: Create an 8x3 array (10–34) and split into 4 sub-arrays
print("Exercise 6:")
array6 = np.arange(10, 34).reshape(8, 3)
print("Original Array:\n", array6)
sub_arrays = np.split(array6, 4)  # 4 equal sub-arrays
print("Splitted Arrays:")
for sub in sub_arrays:
    print(sub)
print("-" * 40)



# Exercise 7: Sort array
# Case 1: by second row
# Case 2: by second column
print("Exercise 7:")
sampleArray7 = np.array([[34, 43, 73],
                         [82, 22, 12],
                         [53, 94, 66]])
print("Original Array:\n", sampleArray7)

# Case 1: sort by second row
sorted_by_row = sampleArray7[:, sampleArray7[1, :].argsort()]
print("Sorted by second row:\n", sorted_by_row)

# Case 2: sort by second column
sorted_by_col = sampleArray7[sampleArray7[:, 1].argsort()]
print("Sorted by second column:\n", sorted_by_col)
print("-" * 40)



# Exercise 8: Print max from axis 0 and min from axis 1
print("Exercise 8:")
sampleArray8 = np.array([[34, 43, 73],
                         [82, 22, 12],
                         [53, 94, 66]])
print("Array:\n", sampleArray8)
print("Max along axis 0 (column-wise):", np.max(sampleArray8, axis=0))
print("Min along axis 1 (row-wise):", np.min(sampleArray8, axis=1))
print("-" * 40)



# Exercise 9: Delete 2nd column and insert new column
print("Exercise 9:")
sampleArray9 = np.array([[34, 43, 73],
                         [82, 22, 12],
                         [53, 94, 66]])
print("Original Array:\n", sampleArray9)
newColumn = np.array([[10], [10], [10]])
modified_array = np.delete(sampleArray9, 1, axis=1)  # delete 2nd column
modified_array = np.insert(modified_array, 1, newColumn, axis=1)  # insert new column
print("Modified Array:\n", modified_array)
print("-" * 40)



# Exercise 10: Create two 2D arrays and plot them
print("Exercise 10:")
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 5, 4], [3, 2, 1]])

print("Array X:\n", x)
print("Array Y:\n", y)

# Flatten arrays for plotting
plt.plot(x.flatten(), label="Array X", marker='o')
plt.plot(y.flatten(), label="Array Y", marker='x')
plt.title("Plot of Two Arrays")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
