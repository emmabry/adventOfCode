with open('data.txt', 'r') as file:
    data = file.read().split('mul')
    toMul = []
    for piece in data:
        if piece[0] == '(':
            piece = piece[1:].split(')')[:-1]
            if len(piece) > 1:
                toMul.append(piece[0])
            else:
                toMul.append(''.join(piece))

print(len(toMul))

total = 0
for nums in toMul:
    nums = nums.split(',')
    try:
        num1 = int(nums[0])
        num2 = int(nums[1])
        total += num1 * num2
    except ValueError:
        print("False")
    except IndexError:
        print("False")

print(total)
