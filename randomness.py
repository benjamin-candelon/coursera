import random
import numpy as np

mu = 0
sigma = 1
population = [random.normalvariate(mu, sigma) for _ in range(10000)]
sample_a = random.sample(population, 500)
sample_b = random.sample(population, 500)
means = [np.mean(random.sample(population, 1000)) for _ in range(100)]
print(np.mean(means))
stds = [np.std(random.sample(population, 1000)) for _ in range(100)]
print(np.mean(stds))
