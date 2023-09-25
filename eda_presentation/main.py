import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('foodhub_order.csv')


print(data.info())
print(data.head())

print(data.head())

print(data.describe())

print(data.isnull().sum())
