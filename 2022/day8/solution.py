from read import read
import os

def is_visible(map, coords):
    (tree_x, tree_y) = coords
    tree = int(map[tree_y][tree_x])
    horizontal = [int(x) for x in map[tree_y]]
    all_directions = [horizontal[:tree_x], horizontal[tree_x+1:]]
    vertical = [int(y[tree_x]) for y in map]
    all_directions.extend([vertical[:tree_y], vertical[tree_y+1:]])
    if [] in all_directions:
        return True
    else:
        for direction in all_directions:
            if len([t for t in direction if t < tree]) == len(direction): return True
    return False

def part1(filename):
    input = read.from_file(filename)
    visible_trees = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if is_visible(input, (x, y)): visible_trees += 1
    return visible_trees

def calculate_scenic_score(map, coords):
    (tree_x, tree_y) = coords
    tree = int(map[tree_y][tree_x])
    horizontal = [int(x) for x in map[tree_y]]
    all_directions = [list(reversed(horizontal[:tree_x])), horizontal[tree_x+1:]]
    vertical = [int(y[tree_x]) for y in map]
    all_directions.extend([list(reversed(vertical[:tree_y])), vertical[tree_y+1:]])

    if [] in all_directions: return 0
    
    score = 1
    for direction in all_directions:
        for d in range(len(direction)):
            if direction[d] >= tree:
                score *= d+1
                break
            elif d == len(direction)-1:
                score *= len(direction)
    return score
    
def part2(filename):
    input = read.from_file(filename)
    highest_score = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            scenic_score = calculate_scenic_score(input, (x, y))
            highest_score = max(highest_score, scenic_score)
    return highest_score

print(part2("{}/input.txt".format(os.path.dirname(__file__))))