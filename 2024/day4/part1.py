with open('input.txt') as f:
    lines = f.readlines()

#allLines = [x.strip() for x in lines]
allLines = lines[:]
allLines.extend([''.join(list(col)) for col in list(zip(*lines))])

col_count = len(lines)
for x in range(col_count-3):
    line = ''
    max_y = col_count-x
    for y in range(max_y):
        line += lines[y][x]
        x+=1
        y+=1
    allLines.append(line)

for y in range(1, col_count-3):
    line = ''
    min_x = col_count-y
    for x in range(min_x):
        line += lines[y][x]
        x+=1
        y+=1
    allLines.append(line)

for x in range(col_count-1, 2, -1):
    line = ''
    max_y = x+1
    y = 0
    for y in range(0, max_y):
        line += lines[y][x]
        x-=1
        y+=1
    allLines.append(line)

for y in range(1, col_count-3):
    line = ''
    min_x = y-1
    for x in range(col_count-1, min_x, -1):
        line += lines[y][x]
        x-=1
        y+=1
    allLines.append(line)

print(allLines)
find_count = 0
for line in allLines:
    for i in range(len(line)):
        if line.startswith("XMAS", i) or line.startswith("SAMX", i):
            find_count+=1
print(find_count)