def is_safe(is_asc, a, b):
    return abs(a-b) > 3 or abs(a-b) < 1 or (is_asc and a > b) or (not is_asc and a < b)

def check_safe(line):
    levels = [int(n) for n in line]
    is_asc = levels[0] < levels[1]
    for i in (range(1, len(levels))):
        a = levels[i-1]
        b = levels[i]
        if is_safe(is_asc, a, b):
            print(a, b, levels)
            return False
    return True

def fix_unsafe(line):
    levels = [int(n) for n in line]
    temp = levels[:]
    temp.pop(0)
    if check_safe(temp):
        return temp
    is_asc = levels[0] < levels[1]
    for i in (range(1, len(levels))):
        a = levels[i-1]
        b = levels[i]
        if is_safe(is_asc, a, b):
            temp = levels[:]
            temp.pop(i-1)
            if check_safe(temp):
                return temp
            else:
                temp = levels[:]
                temp.pop(i)
                if check_safe(temp):
                    return temp
    return line

with open('input.txt') as f:
    lines = [line.split() for line in f.readlines()]

lines = list(map(fix_unsafe, lines))
lines = [x for x in lines if not x == False]
lines = list(filter(check_safe, lines))
print(lines)
print(f"Result {len(lines)}")