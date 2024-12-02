count = 0
max_change = 3
min_change = 1

with open("input.txt") as file:
    for report in file:
        levels = report.strip().split(" ")
        levels = [int(str) for str in levels]
        print(levels)

        maintains_direction = levels == sorted(levels) or levels[::-1] == sorted(levels)
        print(maintains_direction)

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
                count += 1

print(count)
