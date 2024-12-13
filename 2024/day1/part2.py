with open('input.txt') as f:
    lines = f.readlines()

first_list = []
second_list = []
for line in lines:
    x = line.split()
    first_list.append(int(x[0]))
    second_list.append(int(x[1]))

similarity_score = 0
for x in first_list:
    occ = list(filter(lambda y: y == x, second_list))
    similarity_score += x * len(occ)

print(similarity_score)