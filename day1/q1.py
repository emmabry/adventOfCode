with open('ids.txt') as f:
    list1 = []
    list2 = []
    for line in f:
        x = line.split('   ')
        x[1] = x[1].replace('\n', '')
        list1.append(x[0])
        list2.append(x[1])

pairs = []
for i in range(1000):
    pairs.append((min(list1), min(list2)))
    list1.remove(min(list1))
    list2.remove(min(list2))

distances = []
for pair in pairs:
    distance = abs(int(pair[0]) - int(pair[1]))
    distances.append(distance)

total = sum(distances)
print(total)
