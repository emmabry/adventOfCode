with open('data.txt', 'r') as file:
    data = file.read().split('mul')
    toMul = []
    canMul = True
    furtherInspection = []
    for i, item in enumerate(data):
        if "do" in item:
            if "don't" in item:
                if canMul:
                    furtherInspection.append(item)
                canMul = False
            else:
                if not canMul:
                    furtherInspection.append(item)
                elif canMul:
                    toMul.append(item)
                canMul = True
        elif canMul:
            toMul.append(item)

multiply = []


def formatting(item):
    if item[0] == '(':
        item = item[1:].split(')')[:-1]
        if len(item) > 1:
            multiply.append(item[0])
        else:
            multiply.append(''.join(item))


for piece in toMul:
    formatting(piece)

for item in furtherInspection:
    if "do" in item:
        if "don't" in item:
            item = item.split("don't")[0]
        else:
            item = item.split("do")[1]
    formatting(item)

total = 0
for nums in multiply:
    nums = nums.split(',')
    if nums[0].isnumeric() and nums[1].isnumeric():
        total += int(nums[0]) * int(nums[1])

print(total)
