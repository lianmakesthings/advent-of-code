import os

def from_file(filepath):
    with open(filepath) as file:
        Lines = file.readlines()
    return [line.strip() for line in Lines]
