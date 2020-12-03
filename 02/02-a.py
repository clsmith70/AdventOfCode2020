# 02-a.py
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
    for i in string:
        if i == char:
            repcount += 1
    if repcount >= int(range[0]) and repcount <= int(range[1]):
        matchcount += 1

print(matchcount)