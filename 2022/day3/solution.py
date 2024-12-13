from read import read
from string import ascii_letters
import os

priorities = {}
prio = 1
for c in ascii_letters:
    priorities[c] = prio
    prio += 1

def part1(file_path):
    input = read.from_file(file_path)
    backpacks = [[set(item[:len(item)//2]), set(item[int(len(item)/2):])] for item in input]
    shared_items = [list(b[0].intersection(b[1]))[0] for b in backpacks]
    priority_sum = 0
    for i in shared_items:
        priority_sum += priorities[i]
    return priority_sum

def part2(file_path):
    input = read.from_file(file_path)
    i = 0
    priority_sum = 0
    while i < len(input):
        elf1 = set(input[i])
        elf2 = set(input[i+1])
        elf3 = set(input[i+2])
        badge = set.intersection(elf1, elf2, elf3)
        priority_sum += priorities[list(badge)[0]]
        i += 3
        
    return priority_sum

print(part2("{}/input.txt".format(os.path.dirname(__file__))))