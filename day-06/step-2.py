from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

times = lines[0].split(':')[1].replace(' ', '')
distances = lines[1].split(':')[1].replace(' ', '')

race = (int(times), int(distances))
min_time = 0
max_time = 0
moe = 1

for i in range(1,race[0]):
    dist = i * (race[0] - i)
    
    if dist > race[1]:
        if min_time == 0:
            min_time = i

        if i > max_time:
            max_time = i
    else:
        if max_time > 0:
            break

moe *= (max_time - min_time + 1)

print(moe)
