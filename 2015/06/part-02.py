from collections import defaultdict
import re

class LightingConfig:
    def __init__(self):
        self.lights = defaultdict(int)

    def change(self, action, start, end):
        for y in range(start["y"], end["y"] + 1):
            for x in range(start["x"], end["x"] + 1):
                if action == "turn on":
                    self.lights[(x, y)] += 1
                elif action == "toggle":
                    self.lights[(x, y)] += 2
                elif action == "turn off":
                    if self.lights[(x, y)] > 0:
                        self.lights[(x, y)] -= 1

    def get_lit_count(self):
        return sum(self.lights.values())

class Instruction:
    def __init__(self, line):
        self.line = line
        self.pattern = r'(.*) (\d+),(\d+) through (\d+),(\d+)'
        self.parse()

    def parse(self):
        result = re.match(self.pattern, self.line)
        self.action = result.group(1)
        self.start = { "x": int(result.group(2)), "y": int(result.group(3)) };
        self.end = { "x": int(result.group(4)), "y": int(result.group(5)) }

l = LightingConfig()

with open('input.txt', 'r') as file:
    for line in file:
        i = Instruction(line.strip())
        l.change(i.action, i.start, i.end)

print(l.get_lit_count())
