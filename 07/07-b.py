# 07-b.py
from os import read

file = open("input.txt")
data = [line.strip() for line in file.readlines()]
file.close()
