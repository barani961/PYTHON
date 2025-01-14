import numpy as np

rows, cols = map(int, input("Enter the number of rows and columns (space-separated): ").split())
array_2d = np.array([[float(input(f"Enter element at [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

row_index, col_index = map(int, input("Enter the row and column indices for indexing (space-separated): ").split())
indexed_element = array_2d[row_index, col_index]

sorted_array = np.sort(array_2d, axis=None)

print("Original 2D Array:")
print(array_2d)

print(f"Element at index [{row_index}][{col_index}]:", indexed_element)

print("Sorted 2D Array:")
print(sorted_array.reshape(array_2d.shape))  