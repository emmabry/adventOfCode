import csv

lists = []
with open('data.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        lists.append(row)


goodCount = 0
for lst in lists:
    length = len(lst)
    isGood = True
    asc = None
    for i in range(1, length):
        prev = int(lst[i - 1])
        curr = int(lst[i])
        diff = curr - prev

        if abs(diff) < 1 or abs(diff) > 3:
            isGood = False
            break
        if asc is None:
            asc = diff > 0
        elif (asc and diff < 0) or (not asc and diff > 0):
            isGood = False
            break

    if isGood:
        goodCount += 1

print(goodCount)
