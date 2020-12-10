#!/usr/bin/env python3

# Day 10 challenge 
import copy, itertools, operator, math

data = sorted(list(map(lambda l: int(l.strip('\n')), open('input').readlines())))
data = data + [data[-1] + 3]

# Part 1 - 1984
r = [0] + copy.deepcopy(data)
u = list(itertools.starmap(operator.sub, list(zip(data, r))))
print(u.count(1) * u.count(3))

# Part 2 - 3543369523456
cm, clen = [], -1
for n in r:
    if len(r) > r.index(n) + 1 and r[r.index(n) + 1] - n == 3:
        if 0 < clen < 3: cm.append(clen * 2)
        elif clen == 3: cm.append(7)
        clen = -1
    else:
        clen += 1

print(math.prod(cm))

