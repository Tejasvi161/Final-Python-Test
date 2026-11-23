numbers = [2, 3, 10, 6, 4, 8, 1]

min_num = numbers[0]
max_diff = numbers[1] - numbers[0]

for num in numbers[1:]:
    diff = num - min_num

    if diff > max_diff:
        max_diff = diff

    if num < min_num:
        min_num = num

print("Maximum difference:", max_diff)