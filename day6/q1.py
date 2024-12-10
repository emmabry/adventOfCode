with open('realdata.txt', 'r') as f:
    data = f.read().splitlines()

array = [list(line) for line in data if line]
searching = True

# Movement:
while searching:

    searching = False
    for line in array:
        try:
            if '<' in line:
                index = line.index('<')
                if line[index - 1] != '#':
                    line[index] = 'X'
                    line[index - 1] = '<'
                else:
                    line[index] = '^'
                searching = True
            elif '>' in line:
                index = line.index('>')
                if line[index + 1] != '#':
                    line[index] = 'X'
                    line[index + 1] = '>'
                else:
                    line[index] = 'v'
                searching = True
            elif '^' in line:
                index = line.index('^')
                if array[array.index(line) - 1][index] != '#':
                    line[index] = 'X'
                    array[array.index(line) - 1][index] = '^'
                else:
                    line[index] = '>'
                searching = True
            elif 'v' in line:
                index = line.index('v')
                if array[array.index(line) + 1][index] != '#':
                    array[array.index(line) + 1][index] = 'v'
                    line[index] = 'X'
                else:
                    line[index] = '<'
                searching = True

        except IndexError:
            count = 0
            print('exited')
            for line in array:
                for char in line:
                    if char == 'X':
                        count += 1
            print(count)
            break

print(count + 1)