import numpy as np

data_type = [
    ('position', [('x', float), ('y', float)]),
    ('color', [('r', int), ('g', int), ('b', int)])
]

array = np.zeros(3, dtype=data_type)

array['position']['x'] = [1.0, 2.0, 3.0]
array['position']['y']= [4.0, 5.0, 6.0]

array['color']['r'] = [255, 0, 100]
array['color']['g'] = [0, 255, 100]
array['color']['r'] = [0, 0, 255]

print(array)