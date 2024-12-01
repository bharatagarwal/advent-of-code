import re

first_col = []
second_col = []

with open('input.txt') as file:
    for line in file:
        if line == "":
            continue

        first, second = re.split("\s+", line)[0:2]

        first_col.append(int(first))
        second_col.append(int(second))

similarity_score = 0

for num in first_col:
    similarity_score += num * second_col.count(num)

print(similarity_score)
