count = 0

with open('input.txt', 'r') as f:
    for line in f:
        for char in line:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1

print(count)
