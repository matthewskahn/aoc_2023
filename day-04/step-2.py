from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

copies = [0 for i in range(len(lines))]

for card_no, card in enumerate(lines):

    w = set([int(i) for i in card.split('|')[0].split(':')[1].split()])
    m = set([int(i) for i in card.split('|')[1].split()])

    winners = len(m.intersection(w))

    for i in range(1, winners + 1):
        copies[card_no + i] += copies[card_no] + 1

total = sum(copies) + len(lines)

print(total)
    