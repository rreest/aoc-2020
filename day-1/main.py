#!/usr/bin/env python3

# Day 1 challenge 

import itertools

data = [int(a.strip('\n')) for a in open('input').readlines()]
tdata = [1721, 979, 366, 299, 675, 1456]

# Part 1 - Answer: 1020099
print([a * b for a, b in itertools.combinations(data, 2) if a + b == 2020])

# Part 2 - Answer: 49214880
print([a * b * c for a, b, c in itertools.combinations(data, 3) if a + b + c == 2020])

