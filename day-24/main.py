#!/usr/bin/env python3

# Day 24 challenge 

import copy, operator
from ast import literal_eval as make_tuple

data = [x.strip('\n') for x in open('input').readlines()]

VECTORS = {
    'ne': (1,0,-1),
    'nw': (0,1,-1),
    'se': (0,-1,1),
    'sw': (-1,0,1),
    'e': (1,-1,0),
    'w': (-1,1,0)
}

def solve1(paths):
    tiles = {} 
    for p in paths:
        for k, v in VECTORS.items():
            p = p.replace(k, str(v) + '~')
        p = p.strip('~')
        tile = (0,0,0)
        for v in [make_tuple(x) for x in p.split('~')]:
            tile = tuple(map(operator.add, tile, v))

        if tile in tiles:
            tiles[tile] = 'w'
        else:
            tiles[tile] = 'b'
    return (len([x for x in tiles.values() if x == 'b']), tiles)

# Part 1 - 330
solution = solve1(copy.deepcopy(data))
print(solution[0])

# Part 2 - 3711
tiles = solution[1]
for i in range(0,100):
    print(i)
    nutiles = {} 
    # Stage 1 - generate new whites to surround and flip whites that have more than 2 black neighbours
    for k, v in tiles.items():
        if v == 'b':
            for potv in [tuple(map(operator.add, k, x)) for x in VECTORS.values()]:
                if potv not in nutiles:
                    # Generate new white
                    nutiles[potv] = 'w'
                elif nutiles[potv] == 'w':
                    # Since it's been placed we know it has a neighbouring black
                    nutiles[potv] = 'b'
                elif nutiles[potv] == 'b':
                    # Since it's already black it now has more than 2 black neighbours. Make it orange temporarily so it won't be flipped back and forth all the time.
                    nutiles[potv] = 'o'
    for k, v in tiles.items():
        if v == 'b':
            potv = [tuple(map(operator.add, k, x)) for x in VECTORS.values()]
            neighs = len([x for x in potv if x in tiles and tiles[x] == 'b'])
            if neighs == 0 or neighs > 2: nutiles[k] = 'w'
            else: nutiles[k] = 'b'

    # Flip all the oranges we made earlier to white.    
    for k, v in nutiles.items():
        if v == 'o': nutiles[k] = 'w'

    tiles = nutiles

print(len([x for x in tiles.values() if x == 'b']))

