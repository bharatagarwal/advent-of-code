count = 0

with open('input.txt', 'r') as f:
    for line in f:
        for i, char in enumerate(line, 1):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1

            if count == -1:
                print(i)
                break

