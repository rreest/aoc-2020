#!/usr/bin/env python3

# Day 12 solution 

data = [n.strip('\n') for n in open('input').readlines()]

# Part 1 - 938
coord = [0, 0]
waypoint = [10, 1]
vecs = {'N': [0,1],
        'S': [0,-1],
        'E': [1,0],
        'W': [-1,0],
        'F': [1,0]}

def move(c, d, v):
    return list(map(sum, zip(c, map(lambda l: l * d, v))))

def rotate(d, ang, v):
    for i in range(0, ang//90):
        if d == 'R':
            v = (v[1], v[0] * -1)
        else:
            v = (v[1] * -1, v[0])
    return v

for i in data:
    dist = int(i[1:])
    v = i[:1]
    if v in ['R', 'L']:
        vecs['F'] = rotate(v, dist, vecs['F'])
    else:
        coord = move(coord, dist, vecs[v])

print(abs(coord[0]) + abs(coord[1]))

# Part 2 - 54404
coord = [0, 0]
for i in data:
    dist = int(i[1:])
    v = i[:1]
    if v in ['R', 'L']:
        waypoint = rotate(v, dist, waypoint)
    elif v == 'F':
        coord = move(coord, dist, waypoint)
    else:
        waypoint = move(waypoint, dist, vecs[v])

print(abs(coord[0]) + abs(coord[1]))
