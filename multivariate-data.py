import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100)
df = pd.read_csv("./Nhanes.csv")
# print(df.head())
# print(df.columns)
# keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC', 'BMXWAIST']
keep = [column for column in df.columns if 'BM' in column]
# print(df.loc[:,keep])
# print(df[keep])
index_bool = np.isin(df.columns, keep)
# print(index_bool)
print(df.iloc[:, index_bool])
print("Finished")