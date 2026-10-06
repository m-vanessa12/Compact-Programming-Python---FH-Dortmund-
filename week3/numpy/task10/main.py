import numpy as np

points = np.random.random((100,2))

distances = np.sqrt(
    np.sum((points[1:] - points[:-1]) ** 2, axis=1)
)

print ("points:")
print(points)

print("Distances between consecutive points:")
print(distances)