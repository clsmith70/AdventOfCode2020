# 06-a.py
from os import read

file = open("input.txt").read()

answers = file.split('\n\n')
total_count = 0

for a in answers:
    this_count = 0
    a = list(dict.fromkeys(a))
    for b in a:
        if b != '\n':
            this_count += 1
    total_count += this_count

print(total_count)