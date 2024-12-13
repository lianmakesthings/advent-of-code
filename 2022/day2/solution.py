from read import read
import os

def part1(file_path):
    input = read.from_file(file_path)
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for r in range(len(input)):
        moves = input[r].split(' ')
        opponent = points[moves[0]]
        you = points[moves[1]]

        score += you
        if you == 3 and opponent == 1:
            score += 0
        elif you > opponent or (you == 1 and opponent == 3):
            score += 6
        elif you == opponent:
            score += 3
    return score

def part2(file_path):
    input = read.from_file(file_path)
    points = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    score = 0
    for r in range(len(input)):
        (opponent, result) = input[r].split(' ')
        score += points[result]
        if result == 'Y':
            score += points[opponent]
        elif result == 'X':
            you = points[opponent] - 1
            score += you if you > 0 else 3
        elif result == 'Z':
            you = points[opponent] + 1
            score += you if you < 4 else 1
    return score

print(part2("{}/input.txt".format(os.path.dirname(__file__))))