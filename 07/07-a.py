# 07-a.py
from os import read
import re

file = open("testrules.txt")
data = [line.strip() for line in file.readlines()]
file.close()

ruleset = {}
goldbagrules = []

# process the data
for rule in data:
    target = rule.split(' contain ')[0]
    rules = rule.split(' contain ')[1].split(', ')
    rules[-1] = rules[-1].strip('.')
    ruleset[target] = rules

# check for bags that can contain a shiny gold bag  
for rule in ruleset:
    regex = re.compile(r"shiny gold")
    for item in ruleset[rule]:
        if re.search(regex,item):
            goldbagrules.append(rule)

print(goldbagrules)   