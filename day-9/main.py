#!/usr/bin/env python3

# Day 9 challenge 

n = [int(x.strip('\n')) for x in open('input').readlines()]
preamble = n[:25]
bad = 0
for x in n[25:]:
    f = [r for r in preamble if x - r in preamble]
    if not f:    
        bad = x
        break

    preamble = preamble[1:]
    preamble.append(x)

# Part 1 - 18272118
print(bad)

# Part 2 - 2186361
mem = [x for x in n if x < bad]
u = 0
for i in range(0,len(mem)):
    for s in range(0, len(n)):
        slice = mem[s:s+i]
        if sum(slice) == bad:
            u = slice 
    if u:
        break

print(min(u) + max(u))
