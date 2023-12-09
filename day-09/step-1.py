from pathlib import Path
import re

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

lines = [list(map(lambda x: int(x), re.findall(r'-?\d+', line))) for line in lines]

def derivative(arr):
    next = 0
    deltas = [arr[i] - arr[i - 1] for i in range(1, len(arr))]

    if all(n == 0 for n in deltas):
        return arr[-1]
    else:
        next = derivative(deltas)
    return arr[-1] + next

print(sum([derivative(val) for val in lines]))