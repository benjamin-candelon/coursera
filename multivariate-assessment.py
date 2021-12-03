import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)
path = "./Cartwheeldata.csv"
df = pd.read_csv(path)
print(df.head())
# sns.scatterplot(data=df, x='Height', y='Wingspan')
# sns.scatterplot(data=df, x='Height', y='Wingspan', hue='GenderGroup')
# sns.barplot(data=df, x='Glasses', y='CWDistance')
# sns.boxplot(data=df, x='CWDistance', y='Wingspan')
# sns.boxplot(data=df, y='CWDistance') # 12
# sns.boxplot(data=df, y='Wingspan') # 9
sns.barplot(data=df, x='Glasses', y='CWDistance')
# sns.barplot(data=df, x='Glasses', y='CWDistance', hue='GenderGroup')
plt.show()
