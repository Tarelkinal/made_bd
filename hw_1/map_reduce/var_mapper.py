#!/usr/bin/python3

import sys


input_lines = sys.stdin.readlines()
cur_mean = 0
cur_var = 0
count = 0
out = ''

for line in input_lines:
    try:
        cur_var = (cur_var * count) / (count + 1) + count * (cur_mean - float(line))**2 / (count + 1) **2
        cur_mean = (cur_mean * count + float(line)) / (count + 1)
        count += 1
    except:
        continue
        

out += f'{count},{cur_mean},{cur_var}'
sys.stdout.write(out)

