from read import read
import os
import string

def is_in_order(a, b):
    if type(a) != list: a = [a]
    if type(b) != list: b = [b]
    for i in range(max(len(a), len(b))):
        if i >= len(a): return True
        if i >= len(b): return False
        
        compare_a = a[i]
        compare_b = b[i]
        print(compare_a, "vs", compare_b)
        if type(compare_a) == int and type(compare_b) == int:
            if compare_a < compare_b: return True
            elif compare_a > compare_b: return False
        else:
            if type(a[i]) == int: compare_a = [compare_a]
            elif type(b[i]) == int: compare_b = [compare_b]
            in_order = is_in_order(compare_a, compare_b)
            if type(in_order) == bool: return in_order

def bubble_sort(input) -> list:
    for i in range(len(input)):
        for j in range(len(input)-1):
            if not is_in_order(input[j], input[j+1]):
                input[j], input[j+1] = input[j+1], input[j]
    return input

def part1(filepath):
    input = read.from_file(filepath)
    sum = 0
    pair_index = 0
    for i in range(0, len(input), 3):
        pair_index += 1
        print("compare", input[i], input[i+1])
        if is_in_order(eval(input[i]), eval(input[i+1])): 
            print("{} is in order".format(pair_index))
            sum += pair_index
    return sum

def part2(filepath):
    input = read.from_file(filepath)
    divider_a = [[2]]
    divider_b = [[6]]
    input = [eval(l) for l in input if l != ""]
    input.extend([divider_a, divider_b])
    print("input", input)
    sorted = bubble_sort(input)
    print("sorted", sorted)
    return (sorted.index(divider_a)+1) * (sorted.index(divider_b)+1)
    
print(part2("{}/input.txt".format(os.path.dirname(__file__))))