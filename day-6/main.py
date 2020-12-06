#!/usr/bin/env python3

# Day 6 solution

data = open('input').read().strip('\n')
print(data)

# Part 1 - 6662
n = [set(n.replace('\n', ''))  for n in data.split('\n\n')]
print(sum([len(x) for x in n]))

# Part 2 - 3382
u = [[set(x) for x in n.split('\n')] for n in data.split('\n\n')]
print(sum([len(x) for x in list(map(lambda l: l[0].intersection(*l), u))]))
