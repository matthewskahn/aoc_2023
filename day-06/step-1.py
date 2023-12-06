from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()

races = [(int(times[i]), int(distances[i])) for i in range(len(times))]

moe = 1

for race in races:
    min_time = 0
    max_time = 0
    
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
    print(min_time, max_time)
    moe *= (max_time - min_time + 1)

print(moe)
    