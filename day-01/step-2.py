import re
from pathlib import Path

fixits = [
    ["one", "o1e"], 
    ["three", "t3e"],
    ["five", "f5e"], 
    ["nine", "n9e"], 
    ["seven", "7n"], 
    ["two", "t2o"], 
    ["eight", "e8t"]
]

numbers = r"one|two|three|four|five|six|seven|eight|nine|\d"
num_lkp = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pattern = re.compile(numbers)

total = 0

with open(f'{Path(__file__).resolve().parent}/input.txt', "r") as f:
    lines = [line.strip() for line in f]

    for line in lines:
        for (find, replace) in fixits:
            line = line.replace(find, replace)
        vals = pattern.findall(line)
        first = num_lkp[vals[0]] if num_lkp.get(vals[0]) else int(vals[0])
        last = num_lkp[vals[-1]] if num_lkp.get(vals[-1]) else int(vals[-1])
        val = (first * 10) + last
        print(f"{line}: {vals} - {first} {last} - value = ({val}). Running total {total + val}")
        total += val

print(total)

