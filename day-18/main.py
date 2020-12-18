#!/usr/bin/env python3

# Day 18 challenge

data = open('input').read().strip('\n')
tokens = [n for n in data.replace(' ', '')]

precedence = {'+': 1, '*': 1, '(': 0, ')':0} 

def solve2(t, p=1):
    values = []
    ops = []
    i = 0

    while i < len(t):
        n1 = t[i]
        if n1 == '(':
            ops.append(n1)
        elif n1.isdigit():
            values.append(int(n1))
        elif n1 == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                if op == '*':
                    values.append(val1*val2)
                else:
                    values.append(val1+val2)

            ops.pop()
        else:
            while len(ops) != 0 and precedence[ops[-1]] >= precedence[n1]:
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                if op == '*':
                    values.append(val1*val2)
                else:
                    values.append(val1+val2)
            
            ops.append(n1)

        i += 1
                
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        if op == '*':
            values.append(val1*val2)
        else:
            values.append(val1+val2)

    return values[-1]

sums = [int(solve2([n for n in x.replace(' ', '')])) for x in data.split('\n')]
print(sum(sums))

precedence['+'] = 2
sums = [int(solve2([n for n in x.replace(' ', '')], p=2)) for x in data.split('\n')]
print(sum(sums))
