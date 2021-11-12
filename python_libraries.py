import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# import numpy as np
import scipy.stats as stats

pd.set_option('display.max_columns', 100)
path = "./Nhanes.csv"
df = pd.read_csv(path)
# print(df.head(2))
bp = df['BPXSY2']
bp = bp.dropna()
print(bp.describe())
# print("Mean:", bp.mean())
print("Median:", bp.median())
# print("Max:", bp.max())
# print("Min:", bp.min())
# print("Standard deviation:", bp.std())
# print("Variance:", bp.var())
# print(bp.diff().values)
bp_iqr = stats.iqr(bp)
# print("IQR:", bp_iqr)
# print(bp)
# sns.displot(data = bp)
# sns.boxplot(data = bp).set(title="Titel")
# sns.displot(a = bp).set(title="Histogram of bp")
sns.distplot(a = bp).set(title="TBD")
plt.show()

print("Finished")
