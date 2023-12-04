import re
from pathlib import Path

total = 0

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = f.readlines()

    re = re.compile(r'\d')
    for line in lines:
        nums = re.findall(line)
        total += (int(nums[0]) * 10) + int(nums[-1])

print(total)