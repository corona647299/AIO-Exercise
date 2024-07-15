import pandas as pd
import numpy as np

df = pd.read_csv(
    "D:\\Demo-git\\AIO-Exercise\\Module2\\Week1_Numpy\\advertising.csv")

data = df.to_numpy()

# C1
sales_data = data[:, 3]
sales_max = np.max(sales_data)
sales_index = np.argmax(sales_data)
print(sales_max)
print(sales_index)

# C2
tv_data = data[:, 0]
tv_mean = tv_data.mean()
print(tv_mean)

# C3
sales_counter = np.sum(sales_data >= 20)
print(sales_counter)

# C4
sales_cond = sales_data >= 15
radio_data = data[:, 1]
radio_cond = radio_data * sales_cond
radio_mean = np.sum(radio_cond)/np.sum(sales_cond)
print(radio_mean)

# C5
newspaper_data = data[:, 2]
newspaper_mean = newspaper_data.mean()
newspaper_cond = newspaper_data > newspaper_mean

sales_cond2 = sales_data * newspaper_cond
sales_sum = np.sum(sales_cond2)
print(sales_sum)

# C6
sales_mean = sales_data.mean()
score_sales = np.where(
    sales_data < sales_mean, "Bad",
    np.where(sales_data > sales_mean, "Good", "Average"))

print(score_sales[7:10])

# C7
average_index = np.argmin(abs(sales_data - sales_mean))
sales_closet = sales_data[average_index]
score_sales = np.where(
    sales_data < sales_closet, "Bad",
    np.where(sales_data > sales_closet, "Good", "Average"))

print(score_sales[7:10])
