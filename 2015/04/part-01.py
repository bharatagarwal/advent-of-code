import hashlib

input = 'iwrupvqb'
h = ''
i = 0

while (i < 1_000_000_000):
    check_val = input + str(i)
    bin_val = check_val.encode('utf-8')
    md5 = hashlib.md5(bin_val)
    h = md5.hexdigest()

    if h.startswith('00000'):
        break

    i += 1

print(i)
print(h)
