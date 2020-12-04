# 03-a.py
from os import read

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

def count_trees(data, slope_right, slope_down):
    row, column = 0, 0
    num_trees = 0
    num_columns = len(data[0])
    while row < len(data):
        if data[row][column] == '#':
            num_trees += 1
        row += slope_down
        column = (column + slope_right) % num_columns
    return num_trees

print(count_trees(data, 3, 1))