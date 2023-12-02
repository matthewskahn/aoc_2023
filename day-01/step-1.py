import re

total = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

    re = re.compile('\d')
    for line in lines:
        nums = re.findall(line)
        total += (int(nums[0]) * 10) + int(nums[-1])

print(total)