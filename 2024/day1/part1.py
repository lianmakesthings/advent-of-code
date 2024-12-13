with open('input.txt') as f:
    lines = f.readlines()

first_list = []
second_list = []
for line in lines:
    x = line.split()
    first_list.append(int(x[0]))
    second_list.append(int(x[1]))

first_list.sort()
second_list.sort()
distances = [abs(x-y) for (x, y) in zip(first_list, second_list)]

print(sum(distances))