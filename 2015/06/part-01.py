import re

light_grid = [[0]*1000 for _ in range(1000)]

def toggle(light):
    if light == 1:
        return 0
    else:
        return 1

with open ('input.txt', 'r') as file:
    for index, line in enumerate(file):
        pattern = r'(.*) (\d+),(\d+) through (\d+),(\d+)'
        result = re.match(pattern, line.strip())

        action = result.group(1)

        y_start = int(result.group(3))
        y_end = int(result.group(5))

        x_start = int(result.group(2))
        x_end = int(result.group(4))

        for y in range(y_start, y_end + 1):
            if action == "turn on":
               light_grid[y][x_start:x_end + 1] = [1] * (x_end - x_start + 1)
            elif action == "turn off":
               light_grid[y][x_start:x_end + 1] = [0] * (x_end - x_start + 1)
            else:
                for x in range(x_start, x_end + 1):
                    light_grid[y][x] = toggle(light_grid[y][x])


sums = [sum(row) for row in light_grid]
print(sum(sums))
