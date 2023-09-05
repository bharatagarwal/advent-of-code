wrapping_paper = 0

with open('input.txt', 'r') as file:
    for line in file:
        l, w, h = sorted([int(x) for x in line.split('x')])
        wrapping_paper += 3*l*w + 2*w*h + 2*h*l

print(wrapping_paper)
