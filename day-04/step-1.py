from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0

for line in lines:

    w = set([int(i) for i in line.split('|')[0].split(':')[1].split()])
    m = set([int(i) for i in line.split('|')[1].split()])

    winners = len(m.intersection(w))

    if winners:
        total += pow(2, winners - 1)

print(total)