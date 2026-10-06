import numpy as np

array = np.arange(256).reshape(16, 16)

print("Original 16x16:")
print(array)

block_sum = array.reshape(4,4,4,4).sum(axis=(1, 3))

print("sum of each 4x4 block:")
print(block_sum)