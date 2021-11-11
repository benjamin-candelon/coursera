import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# import numpy as np
import scipy.stats as stats

pd.set_option('display.max_columns', 100)
path = "./Nhanes.csv"
df = pd.read_csv(path)
# print(df.head())
bp = df['BPXSY2']
bp = bp.dropna()
# print("Mean:", bp.mean())
# print("Median:", bp.median())
# print("Max:", bp.max())
# print("Min:", bp.min())
# print("Standard deviation:", bp.std())
# print("Variance:", bp.var())
# print(bp.diff().values)
bp_iqr = stats.iqr(bp)
print(bp)
sns.boxplot(data = bp).set(title="Titel")
plt.show()
print("Finished")
