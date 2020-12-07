# 05-b.py

from os import read
import array

def get_seat_id(row, column):
    return (row * 8) + column

def initialize_array(t):
    for i in range(0, 128):
        if i == 0:
            t[i] = [False, False, False, False, False, False, False, False]
        else:
            t.insert(i, [False, False, False, False, False, False, False, False])

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

valid_rows = range(0, 127)
valid_seats = range(0, 7)

seat = [0, 0]
row_array = [[]]
initialize_array(row_array)

# calculat the seat id
def get_seat_id(row, column):
    return (row * 8) + column

for line in data:
    row_list = valid_rows
    column_list = valid_seats

    for char in line:
        if char == 'F':
            # get the row lower half
            row_list = row_list[:int(len(row_list) / 2)]
        elif char == 'B':
            # get the row upper half
            row_list = row_list[int((len(row_list) + 1) / 2):]
        elif char == 'L':
            # get the column lower half
            column_list = column_list[:int(len(column_list) / 2)]
        else:
            # get the column upper half
            column_list = column_list[int((len(column_list) + 1) / 2):]

    row_array[row_list.start][column_list.start] = True

for i in range(1, 126):
    if False in row_array[i]:
        for j in range(1, 6):
            if row_array[i][j] == False and row_array[i][j-1] == True and row_array[i][j+1] == True:
                seat[0] = i
                seat[1] = j

print(f'Seat {seat[1]} in Row {seat[0]}, ID: {get_seat_id(seat[0],seat[1])}') 