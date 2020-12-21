#!/usr/bin/env python3

# Day 21 challenge 

from collections import Counter, OrderedDict

def is_safe(ing):
    for a in allergens:
        fwa = [x for x in foods if a in x[1].split(', ')]
        sus = list(filter(lambda x: ing in x[0].split(' '), fwa))
        if len(sus) == len(fwa):
            return False
    return True
    
data = [x.strip() for x in open('input').readlines()]
foods = [[n.strip(')') for n in x.split(' (contains ')] for x in data]
ingredients = [x.split(' (contains ')[0].split(' ') for x in data]
ingredients = set(x for su in ingredients for x in su)
allergens  = [x.split(' (contains ')[1].strip(')').split(', ') for x in data]
allergens = set(x for su in allergens for x in su)



# Part 1 - 2072

safe_ingredients = set(filter(is_safe, ingredients))

s = 0
for f in [set(x[0].split(' ')) for x in foods]:
    s += len(f.intersection(safe_ingredients))

print(s)



# Part 2 - fdsfpg,jmvxx,lkv,cbzcgvc,kfgln,pqqks,pqrvc,lclnj

nu_foods = []
for f in foods:
    nu_foods.append([set(f[0].split(' ')).difference(safe_ingredients), set(f[1].split(', '))])

matches = {}
alls = allergens.copy()
while alls:
    for a in alls:
        fwa = [x[0] for x in nu_foods if a in x[1]]
        flat = [y for x in fwa for y in x]  
        c = Counter(flat)
        sus = [x for x in c.most_common(2) if x[1] == len(fwa)]
        if len(sus) == 1:
            ming = sus[0][0]
            matches[a] = ming 
            alls.remove(a)

            for i, _ in enumerate(nu_foods):
                if ming in nu_foods[i][0]:
                    nu_foods[i][0].remove(ming)
            
            break

print(','.join(OrderedDict(sorted(matches.items())).values()))
