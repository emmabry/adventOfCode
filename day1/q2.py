with open('ids.txt') as f:
    list1 = []
    list2 = []
    for line in f:
        x = line.split('   ')
        x[1] = x[1].replace('\n', '')
        list1.append(x[0])
        list2.append(x[1])

similarity_score = 0
for i in list1:
    total = 0
    for j in list2:
        if i == j:
            total += 1
    similarity = total * int(i)
    similarity_score += similarity

print(similarity_score)
