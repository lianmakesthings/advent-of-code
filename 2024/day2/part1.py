def is_safe(line):
    levels = [int(n) for n in line]
    print(levels)
    is_asc = levels[0] < levels[1]
    for i in (range(1, len(levels))):
        a = levels[i-1]
        b = levels[i]
        print(a, b)
        if abs(a-b) > 3 or abs(a-b) < 1 or (is_asc and a > b) or (not is_asc and a < b):
            return False
    return True

with open('input.txt') as f:
    lines = [line.split() for line in f.readlines()]

print(f"Result {len(list(filter(is_safe, lines)))}")
