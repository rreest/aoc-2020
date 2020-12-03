#!/usr/bin/env python3

# Day 3 challenge 

import itertools, math

data = [n.strip('\n') * 1000 for n in open('input').readlines()]

def solve(right, d):
    c = itertools.count(right, right)
    return len(list(filter(lambda x: x[next(c)] == '#', d)))

# Part 1: 264
print(solve(3, data[1:]))

# Part 2: 6050183040
print(math.prod([solve(n, data[1:]) for n in range(1, 9, 2)]) * solve(1, data[2::2]))

