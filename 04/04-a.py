# 04-a.py
from os import read

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

def reset_dict(thisdict):
    for entry in thisdict:
        thisdict[entry] = False

def set_key_present(thisdict, datakey):
    for entry in thisdict:
        if entry == datakey:
            thisdict[entry] = True

valid_fields = {'byr': False, 'iyr': False, 'eyr': False,
                'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
valid_passport_count = 0
invalid_passport_count = 0

last_line = data[-1]
for line in data:
    if line == '':
        if False not in valid_fields.values():
            valid_passport_count += 1
        else:
            invalid_passport_count += 1

        reset_dict(valid_fields)
    else:
        values = line.split()

        for value in values:
            set_key_present(valid_fields, value.split(':')[0])
        
        if line == last_line:
            if False not in valid_fields.values():
                valid_passport_count += 1
            else:
                invalid_passport_count += 1

print(f'{valid_passport_count} valid passports and {invalid_passport_count} invalid passports processed')