import re
import functools
from pathlib import Path

num_matcher = re.compile(r"[0-9]+")
sym_matcher = re.compile(r"[^0-9\.]")

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0

for curr_line_no, line in enumerate(lines):
    curr_syms = [l.start() for l in list(sym_matcher.finditer(line))]
    print(line)
    for nums in num_matcher.finditer(line):
        curr = int(nums.group(0))
        print(f"Number: {curr}. Start: {nums.start()}, end: {nums.end()}")
        if nums.start() - 1 in curr_syms or nums.end() in curr_syms:
            print(f"Adding {curr}")
            total += curr
        else:
            other_line = lines[curr_line_no-1] if curr_line_no-1 >= 0 else ""
            prev_syms = [l.start() for l in list(sym_matcher.finditer(other_line))]
            prev = [i if i in prev_syms else None for i in range(nums.start() - 1, nums.end() + 1)]
            
            found_prev = functools.reduce(lambda x, y: x + 1 if y != None else x, prev, 0) > 0

            if found_prev:
                print(f"Found a symbol in previous row")
                total += curr
                continue

            else:
                other_line = lines[curr_line_no+1] if curr_line_no+1 < len(lines) else ""
                next_syms = [l.start() for l in list(sym_matcher.finditer(other_line))]
                next = [i if i in next_syms else None for i in range(nums.start() - 1, nums.end() + 1)]
                print(next)
                found_next = functools.reduce(lambda x, y: x + 1 if y != None else x, next, 0) > 0

                if found_next:
                    print(f"Found a symbol in following row")
                    total += curr        

print(total)