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

first_col.sort()
second_col.sort()

sum_of_differences = 0

for index, col in enumerate(first_col):
    sum_of_differences += abs(second_col[index] - first_col[index])

print(sum_of_differences)
