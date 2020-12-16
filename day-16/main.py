#!/usr/bin/env python3

# Template for solution code 

import math

def validate(value, rule):
    return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]

data = open('input').read().strip('\n')
nearby = [[int(x) for x in n.split(',')] for n in data.split('nearby tickets:\n')[1].split('\n')]
mticket = [int(n) for n in data.split('your ticket:\n')[1].split('\n\n')[0].strip('\n').split(',')]
notes = [n for n in data.split('\n\nyour ticket:\n')[0].split('\n')]
rules = {r.split(': ')[0]: [[int(x) for x in n.split('-')] for n in r.split(': ')[1].split(' or ')] for r in data.split('\n\nyour ticket:\n')[0].split('\n')} 

# Part 1 - 20058
invalid = []
bad_ticket = []
for ticket in nearby:
    for field in ticket:
        valid = False
        for rule in rules.values():
            if validate(field, rule):
                valid = True
                break

        if not valid:
            invalid.append(field)
            bad_ticket.append(ticket)

print(sum(invalid))

# Part 2 - 366871907221
nearby = [n for n in nearby if n not in bad_ticket]

rule_candidates = {k: [] for k, _ in rules.items()}
for i in range(len(nearby[0])):
    field = [n[i] for n in nearby]
    suitable_rules = []
    for rule_name, rule in rules.items():
        valid = [n for n in field if validate(n, rule)]
        if len(valid) == len(field):
            suitable_rules.append(rule_name)
    for r in suitable_rules:
        rule_candidates[r].append(i)


rules_mapped = {}
while rule_candidates:
    r, fid = [n for n in rule_candidates.items() if len(n[1]) == 1][0]
    fid = fid[0]
    rules_mapped[r] = fid
    del rule_candidates[r]
    
    for k in rule_candidates:
        rule_candidates[k].remove(fid)

fv = [mticket[v] for k, v in rules_mapped.items() if 'departure' in k]
print(math.prod(fv))
