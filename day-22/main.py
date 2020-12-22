#!/usr/bin/env python3

# Day 22 challenge 
from itertools import count 
from operator import mul
import copy

data = [[int(y) for y in x.split('\n')] for x in open('input').read().strip('\n').split('\n\n')]

def play1(deck):
    p1, p2 = deck
    while p1 and p2:
        if (c1 := p1.pop(0)) > (c2 := p2.pop(0)):
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    win = [x for x in [p1, p2] if len(x) > 0][0]
    win.reverse()
    return sum(map(lambda x: mul(x[0],x[1]), zip(count(1), win)))

def play2(deck):
    p1, p2 = deck
    prev_games = []
    while p1 and p2:
        if prev_games:
            for game in prev_games:
                if game == (p1, p2):
                    p1.reverse()
                    return (1, sum(map(lambda x: mul(x[0],x[1]), zip(count(1), p1))))
        
        prev_games.append((p1.copy(), p2.copy()))

        c1, c2 = p1.pop(0), p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            win = play2([p1[:c1], p2[:c2]])[0]
            if win == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

        elif c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    winner, win = 1, p1
    if p2: winner, win = 2, p2
    win.reverse()
    return (winner, sum(map(lambda x: mul(x[0],x[1]), zip(count(1), win))))

# Part 1 - 32783
print(play1(copy.deepcopy(data)))

# Part 2 - 33455
print(play2(data))
