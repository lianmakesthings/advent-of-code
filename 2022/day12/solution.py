from read import read
import os
import string

def build_map(input):
    grid = {}
    start_point = None
    end_point = None
    for y in range(len(input)):
        for x in range(len(input[y])):
            h = input[y][x]
            if h == 'S':
                h = 'a'
                start_point = (y, x)
            elif h == 'E':
                h = 'z'
                end_point = (y, x)
            grid[(y, x)] = string.ascii_lowercase.index(h)
    return {'grid': grid, 'start_point': start_point, 'end_point': end_point}

def part1(input_file):
    input = read.from_file(input_file)
    map = build_map(input)
    to_visit = []
    visited = { map['start_point']: 0 }
    to_visit.append((map['start_point']))
    for square in to_visit:
        dist = visited[square]
        print("position", square)
        if square == map['end_point']:
            return dist
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # N, S, E, W
            new_location = (square[0] + direction[0], square[1] + direction[1])
            if new_location in map['grid'] and new_location not in to_visit:
                if map['grid'][new_location] - map['grid'][square] <= 1:
                    visited[new_location] = dist + 1
                    to_visit.append(new_location)

def part2(input_file):
    input = read.from_file(input_file)
    map = build_map(input)

    low_points = [s for s in map['grid'] if map['grid'][s] == 0]
    distances = []
    for p in low_points:
        to_visit = []
        visited = { p: 0 }
        to_visit.append((p))
        for square in to_visit:
            dist = visited[square]
            print("position", square)
            if square == map['end_point']:
                distances.append(dist)
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # N, S, E, W
                new_location = (square[0] + direction[0], square[1] + direction[1])
                if new_location in map['grid'] and new_location not in to_visit:
                    if map['grid'][new_location] - map['grid'][square] <= 1:
                        visited[new_location] = dist + 1
                        to_visit.append(new_location)
    return min(distances)

print(part2("{}/input.txt".format(os.path.dirname(__file__))))