words = ["apple", "ant", "ball", "bat", "cat", "car"]

result = {}

for word in words:
    first = word[0]

    if first in result:
        result[first].append(word)
    else:
        result[first] = [word]

print("Grouped words:", result)