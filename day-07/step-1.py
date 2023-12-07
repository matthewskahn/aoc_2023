from pathlib import Path
from functools import cmp_to_key
from collections import defaultdict

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

lines = list(map(lambda x: x.replace('A', 'E').replace('T', 'A').replace('J', 'B').replace('Q', 'C').replace('K', 'D'), lines))
lines = [[list(map(lambda x: int(x, base=16), l.split()[0])), int(l.split()[1]), None] for l in lines]

FIVE_OF_A_KIND = 30
FOUR_OF_A_KIND = 29
FULL_HOUSE = 28
THREE_OF_A_KIND = 27
TWO_PAIR = 26
ONE_PAIR = 25
HIGH_CARD = 24

def determine_rank(hand: list[int]) -> int:
    cards_by_rank = defaultdict(int)
    for card in hand:
        cards_by_rank[card] += 1

    if len(cards_by_rank) == 1:
        return FIVE_OF_A_KIND + max(cards_by_rank.values())
    elif len(cards_by_rank) == 2:
        return FOUR_OF_A_KIND if max(cards_by_rank.values()) == 4 else FULL_HOUSE
    elif len(cards_by_rank) == 3:
        return THREE_OF_A_KIND if max(cards_by_rank.values()) == 3 else TWO_PAIR
    elif len(cards_by_rank) == 4:
        return ONE_PAIR
    else:
        return HIGH_CARD

def sort_hands(h1, h2):
    c1 = [h1[2]] + h1[0]
    c2 = [h2[2]] + h2[0]

    print(f"Comparing {c1} and {c2}")

    for i in range(len(c1)):
        if c1 > c2:
            return 1
        elif c1 < c2:
            return -1
        
    print("This should not ever happen")
    return 0

for hand in lines:
    hand[2] = determine_rank(hand[0]) 

lines.sort(key=cmp_to_key(sort_hands))

total = 0

for i, val in enumerate(lines):
    total += (i + 1) * val[1]

print(total)