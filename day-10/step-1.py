from pathlib import Path
from operator import add

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

moves = { # (y, x)
    '7': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'F': [(0, 1), (1, 0)],
    '-': [(0,-1), (0,1)],
    '|': [(1,0), (-1,0)],
    'S': [(0, 0)],
}

current = (0, 0)
prev = (0,0)
dist = 1

for i, line in enumerate(lines):
    if 'S' in line:
        current = (i, line.index('S'))
        prev = current
        break

for move in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
    test_next = tuple(map(add, current, move))
    if 0 <= test_next[0] < len(lines) and 0 <= test_next[1] < len(lines[0]) and lines[test_next[0]][test_next[1]] in moves.keys():
        test_next_dests = [tuple(map(add, test_next, test_move)) for test_move in moves[lines[test_next[0]][test_next[1]]]]
        if prev in test_next_dests:
            prev = current
            current = test_next
            break

print(current, prev)

while True:
    dist += 1

    if lines[current[0]][current[1]] == 'S':
        print(f"Back to start")
        break
    else:
        possible_next_moves = moves[lines[current[0]][current[1]]]
        print(f"possible next moves: {possible_next_moves}")
        for next_move in possible_next_moves:
            test_new = tuple(map(add, current, next_move))
            print(f"testing {test_new}")
            if 0 <= test_new[0] < len(lines) and 0 <= test_new[1] < len(lines[0]) and test_new != prev and lines[test_new[0]][test_new[1]] in moves.keys():
                prev = current
                current = test_new 
                print(f"moving from {prev} to {current}")
                break

print((dist - 1)/ 2)