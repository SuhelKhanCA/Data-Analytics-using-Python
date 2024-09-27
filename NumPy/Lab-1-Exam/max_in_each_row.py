# max value in each row an array

import numpy as np 

arr = np.random.randint(1, 100, (5, 5))

print("Matrix is: ", arr)

print("Maximum in each row is: ", np.max(arr, axis=1))
print("Maximum in each column is: ", np.max(arr, axis=0))  