from read import read
import os

def get_value_after_cycles(current_val, cycles, instructions):
    processed_instructions = []
    for i in instructions:
        if i == 'noop':
            processed_instructions.append(i)
        else:
            processed_instructions.extend(['noop', i])
    
    for c in range(cycles):
        if processed_instructions[c] == 'noop':
            continue
        else:
            current_val += int(processed_instructions[c].split(' ')[1])
    return current_val

def part1(filename):
    input = read.from_file(filename)
    sum = 0
    sum += get_value_after_cycles(1, 19, input) * 20
    sum += get_value_after_cycles(1, 59, input) * 60
    sum += get_value_after_cycles(1, 99, input) * 100
    sum += get_value_after_cycles(1, 139, input) * 140
    sum += get_value_after_cycles(1, 179, input) * 180
    sum += get_value_after_cycles(1, 219, input) * 220
    return sum

def draw_line(sprite, processed_instructions):
    line = ""
    for p in range(40):
        i = processed_instructions[p]
        if p in sprite: line += "#"
        else: line += "."
        if i.startswith('addx'):
            new_val = int(i.split(' ')[1])
            sprite = [v+new_val for v in sprite]
    return [line, sprite]

def part2(filename):
    instructions = read.from_file(filename)
    processed_instructions = []
    for i in instructions:
        if i == 'noop':
            processed_instructions.append(i)
        else:
            processed_instructions.extend(['noop', i])
    sprite = [0,1,2]
    for l in range(6):
        [line, sprite] = draw_line(sprite, processed_instructions)
        processed_instructions = processed_instructions[40:]
        print(line)

print(part2("{}/input.txt".format(os.path.dirname(__file__))))