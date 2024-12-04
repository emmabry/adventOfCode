import numpy as np

with open('data.txt', 'r') as f:
    data = f.readlines()

array = np.array([list(line) for line in data if line])

count = 0

word1 = ['X', 'M', 'A', 'S']
word2 = ['S', 'A', 'M', 'X']


for i in range(len(array)):
    for j in range(len(array[i]) - 3):
        if list(array[i][j:j + 4]) == word1:
            count += 1
        if list(array[i][j:j + 4]) == word2:
            count += 1

for j in range(len(array[0])):
    for i in range(len(array) - 3):
        if [array[i + k][j] for k in range(4)] == word1:
            count += 1
        if [array[i + k][j] for k in range(4)] == word2:
            count += 1

for i in range(len(array) - 3):
    for j in range(len(array[0]) - 3):
        if [array[i + k][j + k] for k in range(4)] == word1:
            count += 1
        if [array[i + k][j + k] for k in range(4)] == word2:
            count += 1

for i in range(len(array) - 3):
    for j in range(3, len(array[0])):
        if [array[i + k][j - k] for k in range(4)] == word1:
            count += 1
        if [array[i + k][j - k] for k in range(4)] == word2:
            count += 1

print(count)

