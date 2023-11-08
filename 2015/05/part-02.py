import re

count = 0

def nice(string):
    pair_check = r'([a-z][a-z]).*\1'
    flank_check = r'([a-z]).\1'

    return re.search(pair_check, string) and \
        re.search(flank_check, string)

with open('input.txt', 'r') as file:
    for line in file:
        if nice(line.strip()):
            count += 1

print(count)
