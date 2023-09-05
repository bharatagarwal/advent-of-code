coordinate = [0,0]
robo_santa_coordinate = [0, 0]
houses = set()
houses.add(tuple(coordinate))

def move(direction, coordinates):
    if direction == "^":
        coordinates[1] += 1
    elif direction == "v":
        coordinates[1] -= 1
    elif direction == ">":
        coordinates[0] += 1
    elif direction == "<":
        coordinates[0] -= 1

with open('input.txt', 'r') as file:
    for line in file:
        for i, direction in enumerate(line):
            if direction not in "^v<>":
                continue

            if i % 2 == 0:
                move(direction, coordinate)
                houses.add(tuple(coordinate))
            else:
                move(direction, robo_santa_coordinate)
                houses.add(tuple(robo_santa_coordinate))

print(len(houses))
print(houses)
