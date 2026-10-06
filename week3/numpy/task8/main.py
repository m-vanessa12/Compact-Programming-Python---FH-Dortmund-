import numpy as np

def generate_numbers():
    for i in range(10):

     yield i 

array = np.fromiter(generate_numbers(), dtype=int)

print("Array from generator: ")
print(array)
