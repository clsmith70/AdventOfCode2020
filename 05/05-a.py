# 05-a.py

from os import read


file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

valid_rows = range(0, 127)
valid_seats = range(0, 7)
highest_seat_id = 0

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

    this_seat_id = get_seat_id(row_list.start, column_list.start)
    if this_seat_id > highest_seat_id:
        highest_seat_id = this_seat_id

print(f'Highest Seat ID: {highest_seat_id}')