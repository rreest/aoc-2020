#!/usr/bin/env python3

# Template for solution code 
from intcode import run

data = [n.strip('\n').split(' ') for n in open('input').readlines()]

# Part 1 - 2080
print(run(data))

# Part 2 - 2477
sub = {'jmp': 'nop', 'nop': 'jmp'}
for x in [x for x in enumerate(data) if x[1][0] in sub.keys()]:
    data[x[0]] = [sub[x[1][0]], x[1][1]]
    if run(data)[0] == 1:
        print("Got em")
        print(run(data))
        break
    data[x[0]] = x[1]

