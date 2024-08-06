import numpy as np


def compute_mean(x):
    return np.sum(x) / len(x)


x1 = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean: ", compute_mean(x1))


def compute_median(x):
    size = len(x)
    x = np.sort(x)

    if (size % 2 == 0):
        return (1/2*(x[int(size/2)-1]
                     + (x[int(size/2) + 1 - 1])))
    else:
        return x[int((size+1)/2)-1]


x2 = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(x2))


def compute_std(x):
    mean = compute_mean(x)
    variance = 0
    for i in x:
        variance = variance + (i - mean)**2
    variance = variance / len(x)
    return np.sqrt(variance)


x3 = [171, 176, 155, 167, 169, 182]
print("Std: ", np.round(compute_std(x3), 2))


def compute_correlation_cofficient(x, y):
    N = len(x)
    numerator = N * x.dot(y) - np.sum(x)*np.sum(y)
    denominator = np.sqrt(N*np.sum(np.square(x)) - np.sum(x)**2) \
        * np.sqrt(N*np.sum(np.square(y)) - np.sum(y)**2)

    return np.round(numerator / denominator, 2)


x4 = np.asarray([-2, -5, -11, 6, 4, 15, 9])
y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_cofficient(x4, y))
