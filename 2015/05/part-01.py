vowels = ['a', 'e', 'i', 'o', 'u']
forbidden = ['ab', 'cd', 'pq', 'xy']
alphabet = list("abcdefghijklmnopqrstuvwxyz")

nice_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        forbidden_found = False
        for f in forbidden:
            if f in line:
                forbidden_found = True
                break

        if forbidden_found:
            continue

        double_found = False
        for a in alphabet:
            if 2 * a in line:
                double_found = True
                break

        vowel_count = 0
        for v in vowels:
            if v in line:
                vowel_count += line.count(v)

        if double_found and vowel_count >= 3:
            nice_count += 1

print(nice_count)