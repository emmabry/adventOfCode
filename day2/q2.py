import csv

lists = []
with open('day2/data.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        lists.append(row)


goodCount = 0
for lst in lists:
    isGood = True
    asc = None
    badCount = 0
    prevBad = False

    i = 1
    while i < len(lst):
        curr = int(lst[i])
        if prevBad:
            prev = int(lst[i - 2])
            prevBad = False
        else:
            prev = int(lst[i - 1])
        diff = curr - prev

        if abs(diff) < 1 or abs(diff) > 3:
            isGood = False
            badCount += 1
            prevBad = True
            i += 1

        if asc is None:
            asc = diff > 0
        elif (asc and diff < 0) or (not asc and diff > 0):
            isGood = False
            badCount += 1
            prevBad = True

        if badCount > 1:
            isGood = False
        i += 1

    if badCount <= 1:
        isGood = True

    if isGood:
        goodCount += 1

print(goodCount)
