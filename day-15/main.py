#!/usr/bin/env python3

# Day 15 challenge 

data = open('input').read().strip('\n')

def play(iterations):
    numbers = {int(n): i for i, n in enumerate(data.strip().split(','))}
    last = [n for n, v in numbers.items() if v == len(numbers) - 1][0]
    del numbers[last]
    i = len(numbers)
    while i < iterations:
        age = 0
        if last in numbers:
            age = i - numbers[last]
        
        numbers[last] = i
        last = age
        i += 1
    return numbers

# Part 1 - 203
print([n for n, v in play(2020).items() if v == 2019][0])

# Part 2 - 9007186
print([n for n, v in play(30000001).items() if v == 29999999][0])
