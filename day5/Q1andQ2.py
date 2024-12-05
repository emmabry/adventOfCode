import csv

with open('real_rules.txt', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    data = list(reader)

with open('real_lists.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    instructions = list(reader)

# List for Q1
already_ordered = []
# List for Q2
all_items = []

for lst in instructions:
    sorted = []
    changed = True

    while changed:
        changed = False
        for item in data:
            if item[0] in lst and item[1] in lst:
                if item[0] not in sorted and item[1] not in sorted:
                    sorted.extend(item)
                    changed = True
                elif item[0] in sorted and item[1] not in sorted:
                    sorted.insert(sorted.index(item[0]) + 1, item[1])
                    changed = True
                elif item[1] in sorted and item[0] not in sorted:
                    sorted.insert(sorted.index(item[1]), item[0])
                    changed = True
                elif sorted.index(item[0]) > sorted.index(item[1]):
                    sorted.remove(item[0])
                    sorted.insert(sorted.index(item[1]), item[0])
                    changed = True
    if sorted == lst:
        already_ordered.append(lst)
    all_items.append(sorted)

correct_total = 0
total = 0
# Q1
for order in already_ordered:
    middle = int(len(order) // 2)
    correct_total += int(order[middle])
print(f"Total of already ordered lists is: {correct_total}")

# Q2
for order in all_items:
    middle = int(len(order) // 2)
    total += int(order[middle])
print(f"Total of prev incorrect lists is: {total - correct_total}")
