import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.api as sm
import numpy as np

da = pd.read_csv("./Nhanes.csv")
da.rename(columns={'RIAGENDR': 'GENDER'}, inplace=True)
da.rename(columns={'RIDRETH1': 'RACE'}, inplace=True)
da.rename(columns={'RIDAGEYR': 'AGE'}, inplace=True)
da.rename(columns={'DMDEDUC2': 'EDUC'}, inplace=True)
da["GENDER"] = da.GENDER.replace({1: "Male", 2: "Female"})
# print(da.columns)
# df = df[['BPXDI1', 'BPXDI2', 'BPXSY1', 'BPXSY2']].dropna()
# df.drop(df[df['BPXDI1'] == 0].index, inplace=True)
# df.drop(df[df['BPXDI2'] == 0].index, inplace=True)
# df.to_csv('/home/benjamin/Bureau/test.csv')
# sns.regplot(x='BPXDI1', y='BPXDI2', data=da, fit_reg=False)
# Pearson correlation with Pandas
pearson_corr = da[['BPXDI1', 'BPXDI2', 'BPXSY1', 'BPXSY2']].corr()
# sns.regplot(x='BPXSY1', y='BPXDI1', data=df, fit_reg=False)
# sns.FacetGrid(da, col="RACE", row="GENDER").map(plt.scatter, 'BPXSY1', 'BPXDI1', alpha=0.5)
# print(da.EDUC)
# sns.violinplot(data=da, x='EDUC', y='AGE', hue='GENDER', inner=None, split='true')
da.sort_values(by=['AGE'], inplace=True)
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
da['AGEGRP'] = pd.cut(da.AGE, age_bins)
# da.to_csv('/home/benjamin/Bureau/test.csv')
# sns.violinplot(data=da, x='AGEGRP', y='BMXBMI', hue='GENDER', inner=None, split='true')
# sns.FacetGrid(da, row="GENDER").map(sns.violinplot, 'AGEGRP', 'BMXBMI')
# plt.show()
my_tab = pd.crosstab(da.RACE, da.HIQ210)
my_tab = my_tab.apply(lambda z: z/z.sum(), axis=1)
print(my_tab)
