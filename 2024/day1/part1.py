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
total_distance = 0
for x in range(len(first_list)):
    total_distance += abs(second_list[x] - first_list[x])
print(total_distance)