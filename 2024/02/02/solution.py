import copy

max_change = 3
min_change = 1
count = 0


def remove_one(levels):
    length = len(levels)
    options = []

    for i in range(length):
        op = copy.deepcopy(levels)
        del op[i]
        options.append(op)

    return options


def generate_pairs(levels):
    pairs = []

    for index, num in enumerate(levels):
        if index == len(levels) - 1:
            break

        pairs.append([num, levels[index + 1]])

    return pairs


def maintains_order(levels):
    asc = sorted(levels) == levels
    dsc = sorted(levels) == levels[::-1]

    return asc or dsc


def safe_report(levels):
    if not maintains_order(levels):
        return False

    pairs = generate_pairs(levels)

    for pair in pairs:
        diff = abs(pair[0] - pair[1])
        if diff > max_change or diff < min_change:
            return False

    return True


with open("input.txt") as file:

    for report in file:
        levels = report.strip().split(" ")
        levels = [int(str) for str in levels]

        if safe_report(levels):
            count += 1
            continue
        else:
            for option in remove_one(levels):
                if safe_report(option):
                    count += 1
                    break

print(count)
