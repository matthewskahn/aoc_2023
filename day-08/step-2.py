from pathlib import Path
import re
import math

line_pattern = re.compile(r'[A-Z]{3}')

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

move_seq = lines[0].replace('L', '0').replace('R', '1')
nodes = {}
for line in lines[2:]:
    vals = line_pattern.findall(line)
    nodes[vals[0]] = (vals[1], vals[2])


def findEnd(startNode):
    current_node = startNode
    print(f"starting search at {startNode}")
    moves = 0

    while True:
        current_node = nodes[current_node][int(move_seq[moves % len(move_seq)])]
        moves += 1
        print(moves) if moves % 1000000 == 0 else None
        if current_node[-1] == 'Z':
            break

    return moves

start_nodes = [node for node in nodes if node[-1] == 'A']
print(start_nodes)

required_moves = [findEnd(start_node) for start_node in start_nodes]

lcm = math.lcm(*required_moves)

print(lcm)