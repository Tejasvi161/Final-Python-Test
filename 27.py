my_dict = {'a': 30, 'b': 10, 'c': 20}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Sorted dictionary:", sorted_dict)