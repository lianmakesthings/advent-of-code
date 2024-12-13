import re
import os

# each item is 3 chars + 1 char for space
def read(file_path):
    with open(file_path) as file:
        Lines = file.readlines()
    input = [line[:-1] for line in Lines]
    stack_input = input[:input.index('')]
    stack_input.reverse()
    number_of_stacks = (len(stack_input[0])+1)//4
    stack_input.pop(0)
    stacks = [[] for s in range(number_of_stacks)]
    for line in stack_input:
        for l in range(number_of_stacks):
            letter = line[4*l+1:4*l+2]
            if letter != ' ':
                stacks[l].append(letter)
    
    instruction_input = input[input.index('')+1:]
    instructions = [re.findall("move (\d+) from (\d) to (\d)", i) for i in instruction_input]
    return [stacks, instructions]

def part1(file_path):
    [stacks, instructions] = read(file_path)
    for instruction in instructions:
        [number, from_stack, to_stack] = instruction[0]
        for n in range(int(number)):
            stacks[int(to_stack)-1].append(stacks[int(from_stack)-1].pop())
    return ''.join([stack[-1] for stack in stacks])

def part2(file_path):
    [stacks, instructions] = read(file_path)
    for instruction in instructions:
        [number, from_stack, to_stack] = instruction[0]
        to_move = stacks[int(from_stack)-1][(-int(number)):]
        stacks[int(from_stack)-1] = stacks[int(from_stack)-1][:-int(number)]
        stacks[int(to_stack)-1].extend(to_move)
    return ''.join([stack[-1] for stack in stacks])

print(part2("{}/input.txt".format(os.path.dirname(__file__))))