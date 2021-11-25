# import numpy as np
import numpy as np
import pandas as pd
# import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
df = pd.read_csv("./Nhanes.csv")
df.index = range(1, df.shape[0]+1)
# print(df.head())
my_serie = df[df["RIDAGEYR"] > 60]
my_mean = my_serie['BPXSY1'].head(100)
print(my_mean.mean())
# print(pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,100), 'BPXSY1']))
test = pd.DataFrame({'col1': np.repeat([3, 1], 5), 'col2': range(3, 13)}, index=range(1, 11))
my_mean = pd.Series.mean(test[test.col1 > 2].iloc[range(0, 5), 1])
print(my_mean)
