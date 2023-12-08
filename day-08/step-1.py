from pathlib import Path
import re
line_pattern = re.compile(r'[A-Z]{3}')

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

move_seq = lines[0].replace('L', '0').replace('R', '1')
nodes = {}
for line in lines[2:]:
    vals = line_pattern.findall(line)
    nodes[vals[0]] = (vals[1], vals[2])

current_node = 'AAA'
moves = 0
move_idx = 0

while True:
    current_node = nodes[current_node][int(move_seq[move_idx % len(move_seq)])]
    moves += 1
    move_idx += 1
    print(current_node)
    if current_node == 'ZZZ':
        break

print(moves)