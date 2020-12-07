# 06-b.py
from os import read
from collections import Counter

file = open("input.txt").read()

answers = file.split('\n\n')
total_count = 0

for a in answers:
    this_count = 0
    b = Counter(a)
    group = b['\n'] + 1
    for c in b:
        if c != '\n':
            if b[c] == group:
                this_count += 1
    total_count += this_count

print(total_count)