import warnings
warnings.filterwarnings('ignore')
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

random.seed(1738)
mu = 7
sigma = 1.7
Observations = [random.normalvariate(mu, sigma) for _ in range(100000)]
# sns.distplot(Observations)
# plt.axvline(np.mean(Observations) + np.std(Observations), color = "g")
# plt.axvline(np.mean(Observations) - np.std(Observations), color = "g")
# plt.axvline(np.mean(Observations) + (np.std(Observations) * 2), color = "y")
# plt.axvline(np.mean(Observations) - (np.std(Observations) * 2), color = "y")


print(pd.Series(Observations).describe())
# plt.show()

# SampleA = random.sample(Observations, 100)
# SampleB = random.sample(Observations, 100)
# SampleC = random.sample(Observations, 100)
# fig, ax = plt.subplots()
# sns.distplot(SampleA, ax = ax)
# sns.distplot(SampleB, ax = ax)
# sns.distplot(SampleC, ax = ax)
# plt.show()

mu = 7

sigma = 1.7

Observations = [random.normalvariate(mu, sigma) for _ in range(100000)]

# sns.distplot(Observations)
# plt.axvline(np.mean(Observations) + np.std(Observations), 0, .59, color = 'g')
# plt.axvline(np.mean(Observations) - np.std(Observations), 0, .59, color = 'g')
#
# plt.axvline(np.mean(Observations) + (np.std(Observations) * 2), 0, .15, color = 'y')
# plt.axvline(np.mean(Observations) - (np.std(Observations) * 2), 0, .15, color = 'y')
# plt.show()

from statsmodels.distributions.empirical_distribution import ECDF
ecdf = ECDF(Observations)
plt.plot(ecdf.x, ecdf.y)
plt.axhline(y = 0.025, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observations) - (2 * np.std(Observations)), color = 'y', linestyle='-')
plt.axhline(y = 0.975, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observations) + (2 * np.std(Observations)), color = 'y', linestyle='-')
plt.show()