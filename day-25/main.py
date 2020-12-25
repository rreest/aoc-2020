#!/usr/bin/env python3

# Day 25 challenge 

door = 14012298 
card = 74241
base = 7
mod = 20201227

def break_key(pubkey):
    i = 1
    val = 1
    while True:
        val = (val*base)%mod
        if val == pubkey:
            return (val, i)
        i+=1

def transform(pubkey, loopsz):
    enkey = 1 
    for _ in range(loopsz):
        enkey = (enkey*pubkey)%mod
    return enkey

# Part 1 - 18608573
door_loopsz = break_key(door)[1]
print(transform(card, door_loopsz))
