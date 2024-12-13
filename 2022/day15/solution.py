from read import read
import os
import re

def parse_input(filename):
    input = read.from_file(filename)
    regex = "Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)"
    data = []
    for line in input:
        match = re.search(regex, line)
        if match:
            data.append([(int(match.group(1)), int(match.group(2))), (int(match.group(3)), int(match.group(4)))])
    return data

def calculate_non_beacons_by_row(data, row):
    sensor = data[0]
    beacon = data[1]
    
    dist_x_to_beacon = abs(sensor[0] - beacon[0])
    dist_y_to_beacon = abs(sensor[1] - beacon[1])
    manhattan_distance = dist_x_to_beacon + dist_y_to_beacon
    dist_y_to_row = abs(sensor[1] - row)
    dist_x_range = manhattan_distance - dist_y_to_row
    if dist_x_range >= 0:
        non_beacons = set([sensor[0] + dist_x for dist_x in range(-dist_x_range, dist_x_range+1)])
    else: non_beacons = set([])
    return non_beacons

def part1(filename, row):
    data = parse_input(filename)
    non_beacons = set([])
    for line in data:
        beacon = line[1]
        non_beacons.update(calculate_non_beacons_by_row(line, row))
        if beacon[1] == row:
            non_beacons.discard(beacon[0])
    return len(non_beacons)

def find_beacon(data, max_range):
    all_x = set(range(0, max_range))
    for row in range(0, max_range):
        print("row", row)
        non_beacons = set([])
        beacon_candidates = all_x.difference(non_beacons)
        for line in data:
            beacon_candidates = beacon_candidates.difference(calculate_non_beacons_by_row(line, row))
            # print("beacon_candidates", beacon_candidates)
            if len(beacon_candidates) <= 0: 
                break
        # print("beacons", str(beacons))
        if len(beacon_candidates) > 0:
            return (beacon_candidates.pop(), row)
    return (0,0)

def part2(filename, max_range):
    data = parse_input(filename)
    beacon = find_beacon(data, max_range)
    return beacon[0] * 4000000 + beacon[1]

print(part2("{}/input.txt".format(os.path.dirname(__file__)), 4000000))