#!/bin/bash

DAY=$1

mkdir day-$DAY
pushd day-$DAY
touch input.txt
touch sample.txt
cat << EOF > step-1.py 
from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]


EOF

cat << EOF > step-2.py 
from pathlib import Path

with open(f'{Path(__file__).resolve().parent}/input.txt', 'r') as f:
    lines = [l.strip() for l in f]


EOF

popd
