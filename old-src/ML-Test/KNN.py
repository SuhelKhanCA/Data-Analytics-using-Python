from math import sqrt

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    return sqrt(sum((row1[i] - row2[i])**2 for i in range(len(row1) - 1)))

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = [(train_row, euclidean_distance(test_row, train_row)) for train_row in train]
    distances.sort(key=lambda x: x[1])
    return [distances[i][0] for i in range(num_neighbors)]

# Make a classification prediction
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    return max(set(output_values), key=output_values.count)

# Test the k-NN implementation
dataset = [
    [2.7810836, 2.550537003, 0],
    [1.465489372, 2.362125076, 0],
    [3.396561688, 4.400293529, 0],
    [1.38807019, 1.850220317, 0],
    [3.06407232, 3.005305973, 0],
    [7.627531214, 2.759262235, 1],
    [5.332441248, 2.088626775, 1],
    [6.922596716, 1.77106367, 1],
    [8.675418651, -0.242068655, 1],
    [7.673756466, 3.508563011, 1]
]

# Predict the class for the first data point using k=3
test_row = dataset[0]
num_neighbors = 3
prediction = predict_classification(dataset, test_row, num_neighbors)
print(f'Expected {test_row[-1]}, Got {prediction}.')
