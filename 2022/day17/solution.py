from read import read
import os
import re

rocks = [
        # @@@@
        [[0, 1, 2, 3]], 
        # .@.
        # @@@
        # .@.
        [[1], [0, 1, 2], [1]], 
        # ..@
        # ..@
        # @@@
        [[2], [2], [0, 1, 2]], 
        # @
        # @
        # @
        # @
        [[0], [0], [0], [0]], 
        # @@
        # @@
        [[0, 1], [0, 1]]
    ]

def move_rock(chamber, current_rock, direction):
    new_rock = []
    if direction == ">":
        for line in current_rock:
            new_line = [(x+1, y) for (x, y) in line]
            if max(new_line, key=lambda x: x[0])[0] > 7:
                new_rock.append(line)
            else:
                new_rock.append(new_line)
    elif direction == "<":
        for line in current_rock:
            new_line = [(x-1, y) for (x, y) in line]
            if min(new_line, key=lambda x: x[0])[0] <= 0:
                new_rock.append(line)
            else:
                new_rock.append(new_line)
    else:
        for line in current_rock:
            new_line = [(x, y-1) for x,y in line]
            if any([p in chamber or p[1] == 0 for p in new_line]):
                [chamber.update(l) for l in current_rock]
                new_rock = []
                break
            else:
                new_rock.append(new_line)   
    return (chamber, new_rock)

def part1(filename):
    input = read.from_file(filename)[0]
    chamber = set([(0, 0)])
    fall = False
    input_i = 0
    rock = []
    rock_count = 0
    while rock_count < 2023:
        direction = ""
        
        if len(rock) <= 0:
            r_temp = rocks[rock_count%len(rocks)][:]
            highest_y = max(chamber, key=lambda x: x[1])[1]
            r_temp.reverse()
            for l in range(len(r_temp)):
                rock.append([(x+3, highest_y+4+l) for x in r_temp[l]])
            print("rock_count", rock_count+1)
            # print("chamber", chamber)
            # print("rock", rock)
        elif not fall:
            fall = True
            direction = input[input_i%len(input)]
            input_i += 1
            chamber, rock = move_rock(chamber, rock, direction)
        else:
            fall = False
            chamber, rock = move_rock(chamber, rock, direction)
            if len(rock) <= 0:
                rock_count += 1
    return max(chamber, key=lambda x: x[1])[1]

#print(part2("{}/input.txt".format(os.path.dirname(__file__)), 4000000))