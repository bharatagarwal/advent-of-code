import re

vowels = ('a', 'e', 'i', 'o', 'u')
disallowed_strings = ('ab', 'cd', 'pq', 'xy')
count = 0

def nice(string):
    for dstring in disallowed_strings:
        if dstring in string:
            return False

    vowel_count = 0
    for c in string:
        if c in vowels:
            vowel_count += 1

    double_char_check = r'([a-z])\1'

    return vowel_count >= 3 and re.search(double_char_check, string)

with open('input.txt', 'r') as file:
    for line in file:
        if nice(line.strip()):
            count += 1

print(count)


