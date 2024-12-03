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
            item = item.split("don't")
            formatting(item[0])
        else:
            item = item.split("do")
            formatting(item[1])

total = 0
for i, nums in enumerate(multiply):
    nums = nums.split(',')
    try:
        num1 = int(nums[0])
        num2 = int(nums[1])
        total += num1 * num2
    except ValueError:
        pass
    except IndexError:
        pass

print(total)
