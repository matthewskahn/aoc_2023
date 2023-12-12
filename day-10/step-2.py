from pathlib import Path
from operator import add
import re

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
path = []

for i, line in enumerate(lines):
    if 'S' in line:
        current = (i, line.index('S'))
        path.append(current)
        prev = current
        break

for move in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
    test_next = tuple(map(add, current, move))
    if 0 <= test_next[0] < len(lines) and 0 <= test_next[1] < len(lines[0]) and lines[test_next[0]][test_next[1]] in moves.keys():
        test_next_dests = [tuple(map(add, test_next, test_move)) for test_move in moves[lines[test_next[0]][test_next[1]]]]
        if prev in test_next_dests:
            prev = current
            current = test_next
            path.append(current)
            break

while True:
    dist += 1

    if lines[current[0]][current[1]] == 'S':
        break
    else:
        possible_next_moves = moves[lines[current[0]][current[1]]]
        for next_move in possible_next_moves:
            test_new = tuple(map(add, current, next_move))
            if 0 <= test_new[0] < len(lines) and 0 <= test_new[1] < len(lines[0]) and test_new != prev and lines[test_new[0]][test_new[1]] in moves.keys():
                prev = current
                current = test_new
                path.append(current)
                break

transforms = {
    'F': '┌',
    '7': '┐',
    'L': '└',
    'J': '┘',
    '-': '-',
    '|': '|',
    'S': 'S',
}

# Just prints the loop prettily
for i in range(len(lines)):
    curr_line_nodes = sorted([node[1] for node in path if node[0] == i])
    buf = ''
    for j in range(len(lines[i])):
        if j in curr_line_nodes:
            buf += transforms[lines[i][j]]
        else:
            buf += '.'

    print(buf)

open_segments = []

open = True
start = -1

for i in range(len(lines)):
    curr_line_segs = sorted([node[1] for node in path if node[0] == i])
    open_segments.append([])
    open = True

    for j in range(len(lines[0])):
        if j == 0:
            if j in curr_line_segs:
                open = False
            start = j
        elif open and j in curr_line_segs:
            open = False
            open_segments[i].append(range(start, j))
        elif not open and j not in curr_line_segs:
            open = True
            start = j

    if open:
        open_segments[i].append(range(start, len(lines[0])))

interior_area = 0

for i, line in enumerate(lines):
    if 0 < i < len(lines):
        for seg in open_segments[i]:
            fixup = list(line)
            for j in range(seg.start, seg.stop):
                fixup[j] = '.'
            line = ''.join(fixup)

        for seg in open_segments[i]:
            find_bends = line[0:seg.start]
            crossings = re.findall(r'(\||F-*J|L-*7)', find_bends)

            if len(crossings) % 2 == 1:
                interior_area += len(seg)
                
print(interior_area)