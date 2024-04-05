import numpy as np
import pandas as pd

df = pd.read_csv('/content/carsdata.csv')
#creating new data
new_data = df.dropna()

#1.Generate sample data
np.random.seed(0)
data = np.random.randint(0, 100, 100)


#2.Percentiles: we will be using list
percentiles = np.percentile(data, [25, 50, 75])
#for 25th precentiles:
print("25th percentiles: ", percentiles[0])
#for 50th or median precentiles:
print("50 percentiles:", percentiles[1])
#for 75th precentiles:
print("75 percentiles", percentiles[2])
#for space:
print("")

#3.Standard deviation and variance:
std_dev = np.std(data)
variance = np.var(data)
print("For standard deviation:", std_dev)
print("For variance:", variance)
#for space:
print("")

#4.Correlation:
#Here we have to create new data as data2
data2 = np.random.randint(0, 100, 100)
core = np.corrcoef(data, data2) [0, 1]
print("Correlation is:", core)
print("")

data_matrix = np.random.rand(5, 5)
correlation_matrix = np.corrcoef(data_matrix)
print("Correlation matrix:")
print(correlation_matrix)

data3 = np.random.randint(0, 100, 100)
data4 = np.random.randint(0, 100, 100)
correlation2 = np.corrcoef(data3, data4)[0, 1]
print("Correlation between two unrelated datasets:", correlation2)




print(new_data.to_string())