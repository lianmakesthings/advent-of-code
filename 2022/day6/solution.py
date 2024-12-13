import os

def find_start_marker(input, distinct):
    for i in range(distinct, len(input)):
        last_four_chars = input[i-distinct:i]
        if len(set(last_four_chars)) == distinct:
            return i

def part1(input):
    return find_start_marker(input, 4)

def part2(input):
    return find_start_marker(input, 14)

with open("{}/input.txt".format(os.path.dirname(__file__)), 'r') as f:
    print(part2(f.read()))