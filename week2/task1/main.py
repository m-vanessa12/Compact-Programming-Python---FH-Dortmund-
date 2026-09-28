sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last_elements(item):
    return item[-1]
sorted_list = sorted(sample_list,key=last_elements)

# print(last_elements((4,4)))
print(sorted_list)
