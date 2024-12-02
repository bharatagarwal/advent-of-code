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


def safe_report(levels):
    maintains_direction = levels == sorted(levels) or levels[::-1] == sorted(levels)

    if maintains_direction:
        within_acceptable_diff = True
        pairs = []

        for index, num in enumerate(levels):
            if index == len(levels) - 1:
                break

            pairs.append([num, levels[index + 1]])

        for pair in pairs:
            diff = abs(pair[0] - pair[1])
            if diff > max_change or diff < min_change:
                within_acceptable_diff = False
                break

        if within_acceptable_diff:
            return True
        else:
            return False
    else:
        return False


with open("input.txt") as file:

    for report in file:
        levels = report.strip().split(" ")
        levels = [int(str) for str in levels]

        if safe_report(levels):
            count += 1
            continue
        else:
            options = remove_one(levels)

            for option in options:
                if safe_report(option):
                    count += 1
                    break

print(count)
