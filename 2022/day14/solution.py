from read import read
import os

def build_grid(input):
    rocks = set([])
    for l in input:
        corners = l.split(' -> ')
        for i in range(1, len(corners)):
            a = (int(corners[i-1].split(',')[0]), int(corners[i-1].split(',')[1]))
            b = (int(corners[i].split(',')[0]), int(corners[i].split(',')[1]))
            for x in range(min(a[0], b[0]), max(a[0], b[0])+1):
                for y in range(min(a[1], b[1]), max(a[1], b[1])+1):
                    rocks.add((x, y))
    return rocks

def calculate_sand(grid, outer_edges, bottom):
    new_grid = set(list(grid)[:])
    starting_position = (500, 0)
    at_rest = False
    current_position = starting_position
    while at_rest != True:
        next_positions = [(current_position[0], current_position[1]+1), (current_position[0]-1, current_position[1]+1), (current_position[0]+1, current_position[1]+1)]
        for next in next_positions:
            if next[0] in outer_edges:
                print("{} is in outer edges".format(next))
                at_rest = True
                break
            if next not in new_grid:
                if bottom and next[1] >= bottom:
                    print("{} has fallen to the bottom".format(next))
                    new_grid.add(current_position)
                    at_rest = True
                    break
                print("{} is in free fall".format(next))
                current_position = next
                break

            if next_positions.index(next) == len(next_positions)-1:
                print("{} can't fall further".format(next))
                new_grid.add(current_position)
                at_rest = True
    return new_grid

def part1(input_file):
    input = read.from_file(input_file)
    grid = build_grid(input)
    overflow = False
    sand_count = 0
    outer_edges = [min([x[0] for x in grid])-1, max([x[0] for x in grid])+1]
    while overflow != True:
        new_grid = calculate_sand(grid, outer_edges, None)
        if len(new_grid) == len(grid):
            overflow = True
        else:
            sand_count += 1
            print("sand_count", sand_count)
        grid = new_grid
    return sand_count

def part2(input_file):
    input = read.from_file(input_file)
    grid = build_grid(input)
    bottom = max([x[1] for x in grid]) + 2
    overflow = False
    sand_count = 0
    while overflow != True:
        new_grid = calculate_sand(grid, [], bottom)
        if len(new_grid) == len(grid):
            overflow = True
        else:
            sand_count += 1
            print("sand_count", sand_count)
        grid = new_grid
    return sand_count

print(part2("{}/input.txt".format(os.path.dirname(__file__))))