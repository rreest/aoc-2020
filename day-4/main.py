#!/usr/bin/env python3

# Day 4 challenge 

import re

data = open('input').read().strip('\n').split('\n\n')

# Part 1: 250
n = [u for u in data if u.count(':') - u.count('cid:') == 7]
print(len(n))

# Part 2: 158
n = [dict([i.split(':') for i in re.split(' |\n' , r)]) for r in n]
n = [r for r in n if 2020 <= int(r['eyr']) <= 2030 and len(r['pid']) == 9 and 1920 <= int(r['byr']) <= 2002 
        and 2010 <= int(r['iyr']) <= 2020 and r['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',] 
        and re.match(r"#[0-9a-f]{6}", r['hcl']) and (r['hgt'].endswith('in') and 59 <= int(r['hgt'].strip('in')) 
            <= 76 or r['hgt'].endswith('cm') and 150 <= int(r['hgt'].strip('cm')) <= 193)]
print(len(n))
