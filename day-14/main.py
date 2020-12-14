#!/usr/bin/env python3

# Day 14 challenge 

import itertools

def modify(bmap, value):
    bmap, nvals = bmap[0], []
    for val in value:
        nv = list(bmap)
        for i, v in enumerate('{0:36b}'.format(int(val[1]))):
            if bmap[i] == 'X' and v != ' ':
                nv[i] = v
        nv = "".join(nv).replace('X', '0')
        nvals.append([val[0], nv])

    return nvals


def modify2(bitblock, avset):
    bitmap, nvals = list(bitblock[0]), []
    for address, val in avset:
        nv = bitmap.copy()
        for i, v in enumerate('{0:36b}'.format(int(address))):
            if nv[i] == '0' and v == '1':
                nv[i] = v
        
        p = [nv.copy()]
        for xi, x in enumerate(nv):
            if x == 'X':
                štafen = [[px.copy()[:xi] + [r] + px.copy()[xi+1:] for r in ['0', '1']] for px in p]
                p = p + list(itertools.chain(*štafen))

        pfiltered = [n for n in p if 'X' not in n]
        nvals = nvals + [["".join(n), val]  for n in pfiltered]

    return nvals

data = open('input').read().strip('\n')
blocks = [n.replace('mask = ', '').split('\n') for n in data.split('\nmask = ')]
inners = [[[u.replace('mem[', '') for u in x.split('] = ')] for x in n[1:]] for n in blocks]

# Part 1 - 5055782549997
results = list(itertools.chain(*map(modify, blocks, inners)))

mem = {x[0]: int(x[1], 2) for x in results} 
print(sum([n for n in mem.values() if n>0]))

# Part 2 - 4795970362286
results = list(itertools.chain(*map(modify2, blocks, inners)))

mem = {x[0]: int(x[1]) for x in results} 
print(sum([n for n in mem.values() if n>0]))
