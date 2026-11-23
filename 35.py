def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result

numbers = [1, [2, 3], [4, [5, 6]]]

print("Flattened list:", flatten(numbers))