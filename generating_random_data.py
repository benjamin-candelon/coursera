import numpy as np
np.random.seed(123)
# my_sample = []
# for i in range(3):
#     my_sample.append(np.random.normal(100, 1))
# print(my_sample)

population = np.arange(1, 101)
print(population)
sample = np.random.choice(population, 10)
print(sample)