#!/usr/bin/env python3

# Day 2 challenge

import itertools, re, operator

data = [x.strip().split(': ') for x in open('input').readlines()]
data = itertools.starmap(lambda x, y: (y, re.split(' |-', x)), data)
d1, d2 = itertools.tee(data)

tdata = [('abcde', (1, 3, 'a')), ('cdefg', (1, 3, 'b')), ('ccccccccc', (2, 9, 'c'))]

# Part 1 - 519
a = list(filter(lambda x: int(x[1][0]) <= x[0].count(x[1][2]) <= int(x[1][1]), d1))
print(len(a)) 

# Part 2 - 708
b = [x for x in d2 if operator.xor(x[0][int(x[1][0]) - 1] == x[1][2], x[0][int(x[1][1]) - 1] == x[1][2] )]
print(len(b))

