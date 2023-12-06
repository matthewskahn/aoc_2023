from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

seeds = [int(n) for n in lines[0].split(':')[1].split()]
map_keys = ["seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"]

maps = {}

def compute_dest(source, key):
    for val in maps[key]:
        if source in range(val[1], val[1] + val[2]):
            return val[0] + (source - val[1])
        
    return source

i = 1
current = None

while i < len(lines):
    if lines[i].strip() == "":
        i += 1
        continue
    elif "map" in lines[i]:
        current = lines[i].split(' ')[0]
    else:
        if not maps.get(current):
            maps[current] = []
        maps[current].append(tuple([int(n) for n in lines[i].split()]))

    i += 1

nearest = -1
for seed in seeds:
    dest = [seed]
    for key in map_keys:
        dest.append(compute_dest(dest[-1], key))

    print(dest)
    nearest = dest[-1] if nearest == -1 or dest[-1] < nearest else nearest

print(nearest)
