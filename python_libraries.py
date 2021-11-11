import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

da = pd.read_csv("Nhanes.csv")

# Print out the first few rows of the data
print(da.head())

# print(da.DMDEDUC2.value_counts())
da["DMDEDUC2x"] = da.DMDEDUC2.fillna("Missing")
# print(da.DMDEDUC2x.value_counts())
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
# x = da.DMDEDUC2x.value_counts()  # x is just a name to hold this value temporarily

# print(x.median())
# print(x.quantile(0.5))

a = ((da.BPXSY1 >= 120) & (da.BPXSY2 <= 139))
b = ((da.BPXDI1 >= 80) & (da.BPXDI1 <= 86))
print(np.mean(a | b))
print("Finished")
