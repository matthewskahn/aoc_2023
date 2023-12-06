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

# Determine if two range objects overlap at all
def overlaps(r1, r2):
    return (r1.start <= r2.stop and r1.stop >= r2.start, range(max(r1.start, r2.start), min(r1.stop, r2.stop)))

def compute_dest(source, key):
    out = []
    for seed_range in source:
        hwm = seed_range.start
        for val in maps[key]:
            test_range = range(val[1], val[1] + val[2])
            seed_remaining_range = range(hwm, seed_range.stop)
            overlap, overlap_range = overlaps(test_range, seed_remaining_range)
            
            if overlap:
                offset = val[0] - val[1]
                out.append(range(overlap_range.start + offset, overlap_range.stop + offset))

                if seed_remaining_range.start < overlap_range.start:
                    out.append(range(seed_remaining_range.start, overlap_range.start))

                hwm = overlap_range.stop if seed_remaining_range.stop > overlap_range.stop else seed_remaining_range.stop

        out.append(range(hwm, seed_range.stop)) if hwm < seed_range.stop else None

    return out

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

for key in map_keys:
    maps[key].sort(key=lambda x: x[1])

nearest = -1
seed_ranges = []

for i in range(0,len(seeds),2):
    seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

for seed in seed_ranges:    
    dest = [[seed]]
    for key in map_keys:
        dest.append(compute_dest(dest[-1], key))

    print(dest)

    local_min = sorted(dest[-1], key=lambda x: x.start)[0].start
    nearest = local_min if nearest == -1 or local_min < nearest else nearest

print(nearest)
