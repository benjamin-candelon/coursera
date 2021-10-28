import pandas as pd
cartwheel = "./Cartwheeldata.csv"
nhanes = "./Nhanes.csv"
da = pd.read_csv(nhanes)
print(da.columns)
print(da.DMDEDUC2.max())
print("Finished")