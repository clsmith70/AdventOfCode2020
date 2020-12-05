# 04-b.py
from os import read
import re

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()

def reset_dict(thisdict):
    for entry in thisdict:
        thisdict[entry] = False

def set_key(thisdict, datakey, datavalue):
    for entry in thisdict:
        if entry == datakey:
            thisdict[entry] = datavalue

def check_key(datakey, datavalue, dataset):
    try:
        if datakey == "byr":
            if int(datavalue) in range(1920, 2003):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "iyr":
            if int(datavalue) in range(2010, 2021):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "eyr":
            if int(datavalue) in range(2020, 2031):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "hgt":
            cm_pattern = re.compile(r"19[0-3]|1[5-8][0-9]cm")
            in_pattern = re.compile(r"7[0-6]|59|6[0-9]in")
            if re.match(cm_pattern, datavalue) or re.match(in_pattern, datavalue):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "hcl":
            color_pattern = re.compile(r"^#[0-9a-fA-F]{6}$")
            if re.match(color_pattern, datavalue):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "ecl":
            colors = ['amb','blu','brn','gry','grn','hzl','oth']
            if datavalue in colors:
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
        elif datakey == "pid":
            pid_pattern = re.compile(r"^\d{9}$")
            if re.match(pid_pattern, datavalue):
                set_key(dataset, datakey, True)
            else:
                set_key(dataset, datakey, False)
    except ValueError:
        set_key(dataset, datakey, False)

valid_fields = {'byr': False, 'iyr': False, 'eyr': False,
                'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
present_fields = {'byr': False, 'iyr': False, 'eyr': False,
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
            set_key(present_fields, value.split(':')[0], True)
            check_key(value.split(':')[0], value.split(':')[1], valid_fields)
        
#        if line == last_line:
#            if False not in valid_fields.values() and False not in present_fields.values():
#                valid_passport_count += 1
#            else:
#                invalid_passport_count += 1

print(f'{valid_passport_count} valid passports and {invalid_passport_count} invalid passports processed')
# this code returns 187 valid values, but the correct value is 186
# why did removing the final check that made part 1 correct make part 2 correct?