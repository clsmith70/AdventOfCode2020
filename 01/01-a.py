# 01-a.py
from os import read

file = open("input.txt")
data = [line for line in file.readlines()]
file.close()

value1 = 0
value2 = 0

for i in range(0, len(data) - 1):
    value1 = int(data[i])
    for j in range(i + 1, len(data)):
        if int(data[j]) + value1 == 2020:
            print(value1 * int(data[j]))
