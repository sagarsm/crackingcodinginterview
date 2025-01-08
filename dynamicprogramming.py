num = [1,2,3,4,5,6,7,8,9]

# Initialize three empty arrays
array1, array2, array3 = [], [], []

# Function to return the array with the smallest sum
def get_array_with_min_sum(arrays):
    return min(arrays, key=sum)

# Distribute the elements
for n in reversed(num):
    min_array = get_array_with_min_sum([array1, array2, array3])
    min_array.append(n)

print("Array 1:", array1)
print("Array 2:", array2)
print("Array 3:", array3)

