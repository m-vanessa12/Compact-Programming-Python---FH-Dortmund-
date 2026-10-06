import numpy as np

A = np.random.randint(0, 10, 5)
B = np.random.randint(0, 10, 5)

print("Array A:", A)
print("Array B:", B)

equal = np.array_equal(A, B)

print("Area A and B equal?", equal)