#!/usr/bin/python3

import sys


input_lines = sys.stdin.readlines()
cur_mean = 0
cur_var = 0
cur_count = 0
out = ''

for line in input_lines:
    count, mean, var = map(float, line.split(','))
    cur_var = (cur_var * cur_count + var * count) / (cur_count + count) + count * cur_count * (cur_mean - mean)**2 / (cur_count + count) **2
    cur_mean = (cur_mean * cur_count + mean * count) / (cur_count + count)
    cur_count += count
        

out += f'{count},{cur_mean},{cur_var}'
sys.stdout.write(out)

