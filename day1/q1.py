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
    xmin = min(list1)
    ymin = min(list2)
    pairs.append((xmin, ymin))
    list1.remove(xmin)
    list2.remove(ymin)

distances = []
for pair in pairs:
    x = int(pair[0])
    y = int(pair[1])
    distance = abs(x - y)
    distances.append(distance)

total = sum(distances)
print(total)
