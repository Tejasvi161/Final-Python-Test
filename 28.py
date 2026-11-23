students = [
    {'name': 'Rahul', 'marks': 85},
    {'name': 'Amit', 'marks': 90},
    {'name': 'Priya', 'marks': 95}
]

highest = max(students, key=lambda x: x['marks'])

print("Student with highest marks:", highest['name'])
print("Marks:", highest['marks'])