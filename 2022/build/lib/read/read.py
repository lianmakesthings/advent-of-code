import os

def from_file(filepath):
    with open(filepath) as file:
        Lines = file.readlines()
    return [line.strip() for line in Lines]

def test_input(path):
    with open("{}/test_input.txt".format(path)) as file:
        Lines = file.readlines()
    return [line.strip() for line in Lines]

def input(path):
    with open("{}/input.txt".format(path)) as file:
        Lines = file.readlines()
    return [line.strip() for line in Lines]