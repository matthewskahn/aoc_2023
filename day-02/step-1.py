import re
from pathlib import Path

MAX = {"red": 12, "green": 13, "blue": 14}
pattern = "([0-9]+) (red|blue|green)"
matcher = re.compile(pattern)

total = 0

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

    for line in lines:
        game_number = int(line.split(':')[0].split(' ')[1])
        valid = True
        games = line.split(':')[1]
        matches = matcher.findall(games)
        for match in matches:
            number, color = match
            if int(number) > MAX[color]:
                valid = False
                break

        total += game_number if valid else 0

    print(total)