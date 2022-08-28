## Normal Distribution
## python -m pip install matplotlib

import random
import matplotlib.pyplot as plt

# Distribution: It shows how the values are distributed
# Normal Distribution: A distribution in which values close to the mean are more commonly distributed than values further from the mean
# Histogram: Show frequency distribution of values.

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Normal Distribution -> variance = 1 and mean = 0
samples = []
for i in range(100000):
    samples.append(random.normalvariate(mu=0, sigma=1))
    # samples.append(random.paretovariate(alpha=1))
# print(samples)

plt.hist(samples, bins=200)
plt.show()

# Proving and showing how many times each number is repeated
distro = [0, 0, 0, 0, 0, 0, 0]
for x in samples:
    x = int(abs(x) // 1)
    distro[x] += 1
for i,x in enumerate(distro):
    print(f"Numbers close to {i} have been repeated {x} times")
print(distro)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
samples = []
for i in range(100000):
    samples.append(random.choice([100, 200, 300]))
# print(samples)

plt.hist(samples, bins=10)
plt.show()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
samples = []
for i in range(100000):
    samples.append(random.choice([100, 200, 300, 300]))
# print(samples)

plt.hist(samples, bins=10)
plt.show()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
samples = []
for i in range(100000):
    samples.append(random.choice([50, 50, 50, 100, 200, 300, 300]))
# print(samples)

plt.hist(samples, bins=10)
plt.show()
