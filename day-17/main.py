#!/usr/bin/env python3

# Template for solution code 
import numpy as np

rm = {'#': 1, '.': 0}
rmx = np.array([[rm[y] for y in x] for x in open('input').read().strip('\n').split('\n')])
tmx = np.array([0])
tmx.resize((1, len(rmx), len(rmx)))
tmx[0] = rmx

def part1(smx):
    for _ in range(6):
        # Expand cube
        smx = np.pad(smx, 1)

        # pad the data by 1
        datp = np.pad(smx, 1) 

        for z in range(1, len(datp) - 1):
            for x in range(1, len(datp[0]) - 1):
                for y in range(1, len(datp[0]) - 1):
                    slf = datp[z,x,y]

                    floor = datp[z-1,x-1:x+2,y-1:y+2]
                    etherum = datp[z,x-1:x+2,y-1:y+2]
                    roof = datp[z+1,x-1:x+2,y-1:y+2]
                    
                    # Get sum of neighbours
                    neigh = (np.concatenate((floor, etherum, roof))).sum() - slf
                    #print(floor, etherum, roof, sep='\n')
                    #print(slf)
                    #print(x, y, z)
                    if slf and neigh in [2, 3]:
                        smx[z-1,x-1,y-1] = 1
                    elif not slf and neigh == 3:
                        smx[z-1,x-1,y-1] = 1
                    else:
                        smx[z-1,x-1,y-1] = 0
    return (smx).sum()

# Part 1 - 368
print(part1(tmx.copy()))

def part2(smx):
    from itertools import product
    for _ in range(1):
        print("hey")
        # Expand cube
        smx = np.pad(smx, 1)

        # pad the data by 1
        datp = np.pad(smx, 1) 

        for w in range(1, len(datp) - 1):
            for z in range(1, len(datp[0]) - 1):
                for x in range(1, len(datp[1]) - 1):
                    for y in range(1, len(datp[1]) - 1):
                        slf = datp[w,z,x,y]
                        
                        neigh = 0
                        for dw, dx, dy, dz in product([0, 1, -1], repeat = 4):
                            neigh += datp[w + dw, z + dz, x + dx, y + dy] 
                        
                        neigh -= slf

                        # Get sum of neighbours
                        if slf and neigh in [2, 3]:
                            smx[w-1,z-1,x-1,y-1] = 1
                        elif not slf and neigh == 3:
                            smx[w-1,z-1,x-1,y-1] = 1
                        else:
                            smx[w-1,z-1,x-1,y-1] = 0

    return (smx).sum()


smx = np.array([0])
smx.resize((1, 1, len(tmx[0]), len(tmx[0])))
smx[0] = tmx
print(part2(smx.copy()))

