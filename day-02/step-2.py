import operator
import re
import itertools
from pathlib import Path

cube_pattern = r"([0-9]+) (red|blue|green)"
game_pattern = r"Game (\d)"
cube_matcher = re.compile(cube_pattern)
game_matcher = re.compile(game_pattern)

total = 0

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

    for line in lines:
        MAX = {"red": 0, "green": 0, "blue": 0}
        game_number = int(game_matcher.match(line).group(1))

        games = line.split(':')[1]
        matches = cube_matcher.findall(games)
        for match in matches:
            number, color = int(match[0]), match[1]
            if number > MAX[color]:
                MAX[color] = number

        total += list(itertools.accumulate(MAX.values(), operator.mul))[-1]

    print(total)