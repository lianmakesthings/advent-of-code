from read import read
import os
import math

def move_knots(knot_coords, direction):
    H = knot_coords[0]
    T = knot_coords[1]
    if direction == 'U':
        H = (H[0]+1, H[1])
    elif direction == 'D':
        H = (H[0]-1, H[1])
    elif direction == 'L':
        H = (H[0], H[1]-1)
    elif direction == 'R':
        H = (H[0], H[1]+1)
    else:
        raise ValueError('Invalid direction: {}'.format(direction))
    return follow_head([H, T])

def is_adjacent(knot_coords):
    H = knot_coords[0]
    T = knot_coords[1]
    # horizontal
    if abs(H[1] - T[1]) < 2 and H[0] == T[0]:
        return True
    # vertical
    elif abs(H[0] - T[0]) < 2 and H[1] == T[1]:
        return True
    # diagonal
    elif abs(H[0] - T[0]) < 2 and abs(H[1] - T[1]) < 2:
        return True
    else: return False

def follow_head(knot_coords):
    H = knot_coords[0]
    T = knot_coords[1]
    if not is_adjacent([H, T]):
        dist_y = H[0] - T[0]
        if dist_y > 0: dist_y = 1
        elif dist_y < 0: dist_y = -1
        dist_x = H[1] - T[1]
        if dist_x > 0: dist_x = 1
        elif dist_x < 0: dist_x = -1
        T = (T[0] + dist_y, T[1] + dist_x)
    return [H, T]

def part1(filename):
    input = read.from_file(filename)
    knot_coords = [(0, 0), (0, 0)]
    visited_coords = set([(0, 0)])
    for line in input:
        [direction, count] = line.split(" ")
        for i in range(int(count)):
            knot_coords = move_knots(knot_coords, direction)
            visited_coords.add(knot_coords[1])
    return len(visited_coords)

def part2(filename):
    input = read.from_file(filename)
    knot_coords = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    visited_coords = set([(0, 0)])
    for line in input:
        [direction, count] = line.split(" ")
        for i in range(int(count)):
            print("move knot {} to {}".format(knot_coords[0], direction))
            current_knots = move_knots(knot_coords[:2], direction)
            current_knots.extend(knot_coords[2:])
            for k in range(2, len(knot_coords)):
                new_knots = current_knots[:k-1]
                new_knots.extend(follow_head([current_knots[k-1], knot_coords[k]]))
                new_knots.extend(current_knots[k+1:])
                current_knots = new_knots
            visited_coords.add(current_knots[-1])
            knot_coords = current_knots
    return len(visited_coords)

print(part2("{}/input.txt".format(os.path.dirname(__file__))))