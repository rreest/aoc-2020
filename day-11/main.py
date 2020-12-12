#!/usr/bin/env python3

# Day 11 challenge 

import numpy 

data = [['.'] + [x for x in n.strip('\n')] + ['.'] for n in open('input').readlines()]
data = [['.' for _ in range(len(data[0]))]] + data + [['.' for _ in range(len(data[0]))]]

def update(grid, x, y):
    newGrid = grid.copy()
    for i in range(x):
        for j in range(y):
            if grid[i, j] == '.':
                continue

            total = str(grid[i, (j-1)] + grid[i, (j+1)] +
                         grid[(i-1), j] + grid[(i+1), j] +
                         grid[(i-1), (j-1)] + grid[(i-1), (j+1)] +
                         grid[(i+1), (j-1)] + grid[(i+1), (j+1)]).count('#')

            if grid[i, j]  == '#':
                if (total > 3):
                    newGrid[i, j] = 'L'
            else:
                if total == 0:
                    newGrid[i, j] = '#' 

    grid[:] = newGrid[:]
    return grid


# Part 1 - 2164
fdata = numpy.array(data.copy())
while True: 
    ngrid = update(fdata.copy(), len(fdata), len(fdata[0]))
    if (ngrid==fdata).all():
        break
    fdata = ngrid

print((fdata == '#').sum())

# Part 2 - 1974
def get_first(ray):
    for r in ray:
        if r in ['#', 'L']:
            return r
    return '.'

def update2(grid, x, y):
    newGrid = grid.copy()
    for i in range(x):
        for j in range(y):
            if grid[i, j] == '.':
                continue

            rj = (y-j-1)
            si = min((i,j)) 
            rsi = min((i, rj))

            total = get_first(grid[i][j+1:]) # Right - OK
            total += get_first(numpy.flip(grid[i][:j])) # Left - OK
            total += get_first(grid[:, j][i+1:]) # Down - OK
            total += get_first(numpy.flip(grid[:, j][:i])) # Up - OK
           
            total += get_first(numpy.diag(grid, j + (-1 * i))[si+1:])            
            total += get_first(numpy.flip(numpy.diag(grid, j + (-1 * i))[:si]))            
            total += get_first(numpy.diag(numpy.fliplr(grid), rj + (-1 * i))[rsi+1:])
            total += get_first(numpy.flip(numpy.diag(numpy.fliplr(grid), rj + (-1 * i))[:rsi]))            
            total = total.count('#')

            if grid[i, j]  == '#':
                if (total > 4):
                    newGrid[i, j] = 'L'
            else:
                if total == 0:
                    newGrid[i, j] = '#' 

    grid[:] = newGrid[:]
    return grid

fdata = numpy.array(data.copy())
while True:
    ngrid = update2(fdata.copy(), len(fdata), len(fdata[0]))
    if (ngrid==fdata).all():
        break
    fdata = ngrid

print((fdata == '#').sum())

