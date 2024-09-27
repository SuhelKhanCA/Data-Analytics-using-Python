# Average of Diagonal of numpy array

import numpy as np

arr = np.random.randint(1, 100, (5, 5))
print(arr)

sum = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i == j:
            sum += arr[i][j]
print(sum / len(arr))


for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i + j == 5 - 1:
            sum += arr[i][j]
print(sum / len(arr))