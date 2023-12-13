from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [list(l.strip()) for l in f]

def expand_spacetime(arr):
    i = 0;
    while True:
        if i < len(arr):
            if all([x in ['*','.'] for x in arr[i]]):
                arr.insert(i, ['*'] * len(arr[i]))
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
        min_x = min(g1[1], g2[1])
        max_x = max(g1[1], g2[1])
        min_y = min(g1[0], g2[0])
        max_y = max(g1[0], g2[0])

        test_x = lines[g1[0]][min_x:max_x]
        test_y = [lines[i][g1[1]] for i in range(min_y, max_y)]

        x_millions = sum([1 if x == '*' else 0 for x in test_x])
        y_millions = sum([1 if x == '*' else 0 for x in test_y])

        x_dist = len(test_x) - x_millions + (999_999 * x_millions)
        y_dist = len(test_y) - y_millions + (999_999 * y_millions)

        total_distance += x_dist + y_dist

print(total_distance)