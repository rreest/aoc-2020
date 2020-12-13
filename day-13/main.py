#!/usr/bin/env python3

# Day 13 challenge 

data = [n.strip() for n in open('input').readlines()]
ts = int(data[0])
lines = [int(n) for n in data[1].split(',') if n != 'x']

# Part 1 - 2406
mapped = [[(n, x) for x in range(0, ts + 100000, n)] for n in lines]
mapped = [i for s in mapped for i in s]

shortest = min(filter(lambda l: l[1] > ts,mapped), key=lambda l: abs(l[1] - ts))

print(abs(shortest[1] - ts) * shortest[0])

# Part 2 - 225850756401039
rawlines = [n for n in data[1].split(',')]

n = 1
step = 1

for bus in lines:
    index = rawlines.index(str(bus))
    while ((n + index) % bus != 0):
        n += step
    step *= bus

print(n)

