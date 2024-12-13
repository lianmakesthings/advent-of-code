import re
with open('input.txt') as f:
    lines = f.readlines()

sum = 0
execute = True
for line in lines:
    matches = re.findall("(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", line)
    for m in matches:
        print(m, m[0], m[1], m[2])
        if m[0] == "do()":
            execute = True
        elif m[0] == "don't()":
            execute = False
        elif execute and "mul" in m[0]:
            print(m[1], m[2])
            sum += int(m[1]) * int(m[2])
print(sum)