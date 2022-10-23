#!/usr/bin/python3

import sys


input_lines = sys.stdin.readlines()
cur_mean = 0
count = 0
out = ''

for line in input_lines:
    if line is not None:
        cur_mean = (cur_mean * count + float(line)) / (count + 1)
        count += 1
        

out += f'{count},{cur_mean}'
sys.stdout.write(out)

