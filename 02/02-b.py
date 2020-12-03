# 02-b.py
from os import read

file = open("input.txt")
data = [line for line in file.readlines()]
file.close()

matchcount = 0

for line in data:
    record = line.split(' ')
    range = record[0].split('-')
    char = record[1].replace(':','')
    string = record[2]

    repcount = 0
    if string[int(range[0]) - 1] == char:
        if string[int(range[1]) - 1] != char:
            matchcount += 1
    else:
        if string[int(range[1]) - 1] == char:
            matchcount += 1

print(matchcount)