coordinate = [0,0]
houses = set(tuple(coordinate))

with open('input.txt', 'r') as file:
    for line in file:
        for direction in line:
            if direction == "^":
                coordinate[1] += 1
            elif direction == "v":
                coordinate[1] -= 1
            elif direction == ">":
                coordinate[0] += 1
            elif direction == "<":
                coordinate[0] -= 1

            houses.add(tuple(coordinate))


print(len(houses))
