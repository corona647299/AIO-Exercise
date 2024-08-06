import pandas as pd
import numpy as np

data = pd.read_csv(r"Week4_Statistics\advertising.csv")
x1 = data['TV']
y1 = data['Radio']


def correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    corr = numerator / denominator
    return corr


corr_xy = correlation(x1, y1)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(
            f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

x2 = data['Radio']
y2 = data['Newspaper']

result = np.corrcoef(x2, y2)
print(result)

data_corr = data.corr()
print(data_corr)

import matplotlib . pyplot as plt
import seaborn as sns

plt.figure(figsize = (10,8))
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()