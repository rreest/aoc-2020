#!/usr/bin/env python3

# Day 19 challenge

import itertools

data = [n.strip() for n in open('input').readlines()]
data = [n.split(': ') for n in data]

msgs = [n[0] for n in data if n != '' and len(n) == 1]

def solve(rules_tmp):
    rules = {x[0]: x[1][1]for x in rules_tmp.items() if x[1][1] in ['a', 'b']}
    for x in rules:
        del rules_tmp[x]

    # While not all rules have been processed
    while len(rules_tmp) > 0:
        print("baa")
        # Get all rules that can be solved this iteration
        solvable_rules = [x[0] for x in rules_tmp.items() if set(x[1].replace('| ', '').split(' ')).issubset(set(rules.keys()))]
        # Solve the rule
        for sr in solvable_rules:
            # Collapse the string for simplicity
            rulestr = rules_tmp[sr].split(' ')
            # There will be a rule and total rules. All rules will be put in a list and zipped with corresponding keys
            crule = []
            crules = set()
            for token in rulestr:
                if token == '|':
                    # We found a separator token meaning the current rule group has ended. Add it to the rules and clear the current rule buffer to allow creation of the next rule (guaranteed to follow)
                    try:
                        crules.add(''.join(crule))
                    except TypeError:
                        crules = crules.union(set([''.join(n) for n in itertools.product(*crule)]))

                    crule.clear()
                else:
                    # We found a reference to another rule, so get the value of that from our already solved rules (guaranteed to be there) and append it to the current rule. In a sense this is literally just translating.
                    crule.append(rules[token])

            # Finally we will be left with the last rule buffer which can now be collapsed and added to the list of rules.
            try:
                crules.add(''.join(crule))
            except TypeError:
                combs = [n for n in itertools.product(*crule) for x in n]
                for syl in combs:
                    crules.add(''.join(syl))

            # Add all the rules we created to the global dictioanry
            rules[sr] = crules

        for x in solvable_rules:
            del rules_tmp[x]

    return len([n for n in msgs if n in rules['0']])

# Part 1 - 134 
print(solve({n[0]:n[1] for n in data if len(n) > 1}))

# Part 2 theoretically works if you have gigabytes of ram lol
p2rules = {n[0]:n[1] for n in data if len(n) > 1}
p2rules[8] = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42"
p2rules[11] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31"

print(solve(p2rules))
