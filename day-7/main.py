#!/usr/bin/env python3

# Day 7 solution 

data = open('input').read().strip('\n')

rules = [n.split(' bags contain ') for n in data.split('\n')]
ngraph = {n[0]: n[1].split(', ') for n in rules}
graph = {}
for k, v in ngraph.items():
    if v[0] == 'no other bags.':
        graph[k] = []
    else:
        s = [[n.strip('.').replace(' bags', '').replace(' bag', '')[2:]] * int(n[:2]) for n in v]
        graph[k] = [item for sublist in s for item in sublist]

# Part 1 - 355
def has_gold(nd):
    if not graph[nd]:
        return
    if 'shiny gold' in graph[nd]:
        return True
    for n in set(graph[nd]):
        if has_gold(n):
            return True

print(len([n for n in graph.keys() if has_gold(n)]))

# Part 2 - 5312
def get_children(nd):
    all = [nd]
    for nod in graph[nd]:
        all = all + get_children(nod)
    return all

print(len(get_children('shiny gold')) - 1)
