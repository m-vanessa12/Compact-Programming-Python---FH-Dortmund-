import numpy as np

array = np.random.uniform(0, 10, 5)

print("Original array:")
print(array)


print("Method 1:", array.astype(int))
print("Method 2:", np.floor(array))
print("Method 3:", np.trunc(array))
print("Method 4:", array // 1)
print("Method 5:", array - array % 1)
