# 03-b.py
from os import read

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

slope_rates = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def trees_product(tree_map, slopes):
    num_trees = [count_trees(tree_map, right, down) for (right, down) in slopes]
    return product(num_trees)

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

print(trees_product(data, slope_rates))