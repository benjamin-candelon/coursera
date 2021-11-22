# import numpy as np
import pandas as pd
# import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
df = pd.read_csv("./Nhanes.csv")
df.index = range(1,df.shape[0]+1)
print(df.head())