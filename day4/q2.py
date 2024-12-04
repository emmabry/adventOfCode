with open('data.txt', 'r') as f:
    data = f.readlines()
    array = [[char for char in line] for line in data]

count = 0

try:
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'M' and array[i+1][j + 1] == 'A':
                if array[i+2][j] == 'S' and array[i][j+2] == 'M' and array[i+2][j+2] == 'S':
                    count += 1
                elif array[i+2][j] == 'M' and array[i][j+2] == 'S' and array[i+2][j+2] == 'S':
                    count += 1
            elif array[i][j] == 'S' and array[i+1][j+1] == 'A':
                if array[i+2][j] == 'M' and array[i][j+2] == 'S' and array[i+2][j+2] == 'M':
                    count += 1
                elif array[i+2][j] == 'S' and array[i][j+2] == 'M' and array[i+2][j+2] == 'M':
                    count += 1
except IndexError:
    pass

print(count)
