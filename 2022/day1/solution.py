from read import read

def part1(file_path):
    input = read.from_file(file_path)
    calories = [0]
    for line in input:
        if not line:
            calories.append(0)
            continue
        print(calories[-1])
        calories[-1] += int(line)
    return max(calories)

def part2(file_path):
    input = read.from_file(file_path)
    calories = [0]
    for line in input:
        if not line:
            calories.append(0)
            continue
        print(calories[-1])
        calories[-1] += int(line)

    return sum(sorted(calories)[-3:])
    