from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [list(l.strip()) for l in f]

def expand_spacetime(arr):
    i = 0;
    while True:
        if i < len(arr):
            if all([x == '.' for x in arr[i]]):
                arr.insert(i, ['.'] * len(arr[i]))
                i += 2
            else:
                i += 1
        else:
            break

    return arr

def transpose(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

lines = expand_spacetime(lines)
print(len(lines))
lines = transpose(lines)
lines = expand_spacetime(lines)
print(len(lines))
lines = transpose(lines)

[print(''.join(line)) for line in lines]

galaxies = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == '#']

total_distance = 0

for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        # print(f"Distance between {i} and {j} is {abs(g1[0] - g2[0]) + (abs(g1[1] - g2[1]))}")
        total_distance += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(total_distance)