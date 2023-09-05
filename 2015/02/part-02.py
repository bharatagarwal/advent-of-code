ribbon_length = 0

with open('input.txt', 'r') as file:
    for line in file:
        l, w, h = sorted([int(x) for x in line.split('x')])
        ribbon_length += 2*(l+w) + l*w*h

print(ribbon_length)
