import re
import itertools
from pathlib import Path

num_matcher = re.compile(r"[0-9]+")
sym_matcher = re.compile(r"[\*]")

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0

for curr_line_no, line in enumerate(lines):
    curr_syms = [l.start() for l in list(sym_matcher.finditer(line))]
    print(line)
    for sym in curr_syms:
        adjacent_numbers = []
        ratio = 1
        
        # previous line
        prev_line = lines[curr_line_no-1] if curr_line_no-1 >= 0 else ""
        prev_nums = [(int(l.group(0)), range(l.start() - 1, l.end() + 1)) for l in list(num_matcher.finditer(prev_line))]

        for num in prev_nums:
            if sym in num[1]:
                adjacent_numbers.append(num[0])
                ratio *= num[0]

        # current line
        curr_nums = [(int(l.group(0)), [l.start() - 1, l.end()]) for l in list(num_matcher.finditer(line))]
        
        for num in curr_nums:
            if sym in num[1]:
                adjacent_numbers.append(num[0])
                ratio *= num[0]

        # next line
        next_line = lines[curr_line_no+1] if curr_line_no+1 < len(lines) else ""
        next_nums = [(int(l.group(0)), range(l.start() - 1, l.end() + 1)) for l in list(num_matcher.finditer(next_line))]

        for num in next_nums:
            if sym in num[1]:
                adjacent_numbers.append(num[0])
                ratio *= num[0]

        if len(adjacent_numbers) == 2:
            print(f"Gear at location {sym} added to total. Touches {adjacent_numbers}")
            total += ratio
        elif len(adjacent_numbers) > 2:
            print(f"Gear at location {sym} NOT added to total. Touches {adjacent_numbers}")

print(total)