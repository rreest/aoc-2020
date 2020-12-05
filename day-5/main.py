#!/usr/bin/env python3

# Day 5 solution 

data = [n.strip('\n') for n in open('input').readlines()]

def leap(rn, t):
    if len(rn) == 1:
        return rn[0]
    u = len(rn)//2
    if t[0] in ['F', 'L']:
        si, ei = rn[0], rn[u]
    else:
        si, ei = rn[u], rn[-1] + 1
    return leap(range(si, ei), t[1:])
    
# Part 1 - 965
total = [leap(range(0, 128), n[:-3]) * 8 + leap(range(0, 8), n[-3:]) for n in data]
print(max(total))

# Part 2 - 524
x = [n + 1 for n in sorted(total) if n + 1 not in total and n + 2 in total]
print(x[0])

