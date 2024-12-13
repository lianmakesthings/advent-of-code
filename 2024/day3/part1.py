import re
with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    matches = re.findall("(mul\((\\d{1,3}),(\\d{1,3})\))", line)
    for m in matches:
        sum += int(m[1])*int(m[2])
print(sum)