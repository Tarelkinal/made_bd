#!/usr/bin/python3

import sys


input_lines = sys.stdin.readlines()
cur_mean = 0
cur_count = 0
out = ''

for line in input_lines:
    count, mean = map(float, line.split(','))
    cur_mean = (cur_mean * cur_count + mean * count) / (cur_count + count)
    cur_count += count
        

out += f'{count},{cur_mean}'
sys.stdout.write(out)

