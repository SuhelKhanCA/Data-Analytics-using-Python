# Finding maximum of average of rows of a numpy array

import numpy as np

arr = np.random.randint(1, 100, (5, 6))

avg = np.mean(arr, axis=1)

print("Average is: ", avg)
print("Max of these: ", max(avg))