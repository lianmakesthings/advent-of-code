from read import read
import os

def part1(file_path):
    input = read.from_file(file_path)
    assignments = [[[int(number) for number in a.split('-')] for a in pair.split(',')] for pair in input]

    count = 0
    for pair in assignments:
        first = set(range(pair[0][0], pair[0][1]+1))
        second = set(range(pair[1][0], pair[1][1]+1))
        overlap = set.intersection(first, second)
        if overlap == first or overlap == second:
            count += 1
    return count

def part2(file_path):
    input = read.from_file(file_path)
    assignments = [[[int(number) for number in a.split('-')] for a in pair.split(',')] for pair in input]
    
    count = 0
    for pair in assignments:
        if pair[0][1] >= pair[1][0] and pair[1][1] >= pair[0][0]:
            count += 1
    return count


print(part2("{}/input.txt".format(os.path.dirname(__file__))))