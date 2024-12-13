from read import read
import os
import re

def find_adjacent_cubes(cube, all_cubes):
    adjacent_cubes = []
    for test_cube in all_cubes:
        if test_cube == cube:
            continue
        dist_x = abs(cube[0] - test_cube[0])
        dist_y = abs(cube[1] - test_cube[1])
        dist_z = abs(cube[2] - test_cube[2])
        all_dist = [dist_x, dist_y, dist_z]
        if len([d for d in all_dist if d <= 1]) == 3 and len([d for d in all_dist if d == 0]) == 2:
            adjacent_cubes.append(test_cube)
    return adjacent_cubes

def find_holes(cubes):
    holes = []
    range_x = range(min([cube[0] for cube in cubes]), max([cube[0] for cube in cubes])+1)
    range_y = range(min([cube[1] for cube in cubes]), max([cube[1] for cube in cubes])+1)
    range_z = range(min([cube[2] for cube in cubes]), max([cube[2] for cube in cubes])+1)
    for x in range_x:
        for y in range_y:
            for z in range_z:
                coords = (x, y, z)
                cubes_on_x = [cube for cube in cubes if cube[1] == y and cube[2] == z]
                cubes_on_y = [cube for cube in cubes if cube[0] == x and cube[2] == z]
                cubes_on_z = [cube for cube in cubes if cube[0] == x and cube[1] == y]
                if coords not in cubes and len(cubes_on_x) >= 2 and len(cubes_on_y) >= 2 and len(cubes_on_z) >= 2:
                    holes.append(coords)
    return holes

def part1(filename):
    input = [[int(c) for c in line.split(',')] for line in read.from_file(filename)]
    cubes = [(x, y, z) for [x, y, z] in input]
    exposed_sides = 0
    for cube in cubes:
        print("cube", cube)
        adjacent_cubes = find_adjacent_cubes(cube, cubes)
        exposed_sides += (6 - len(adjacent_cubes))
    return exposed_sides

def part2(filename):
    input = [[int(c) for c in line.split(',')] for line in read.from_file(filename)]
    cubes = [(x, y, z) for [x, y, z] in input]
    holes = find_holes(cubes)
    cubes.extend(holes)
    exposed_sides = 0
    for cube in cubes:
        print("cube", cube)
        adjacent_cubes = find_adjacent_cubes(cube, cubes)
        exposed_sides += (6 - len(adjacent_cubes))
    return exposed_sides

print(part2("{}/input.txt".format(os.path.dirname(__file__))))