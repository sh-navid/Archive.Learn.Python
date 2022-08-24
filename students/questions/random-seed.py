import random

# Random data is not a real random; its pseudo-random.

# Use "seed" to achieve deterministic random data; seed 
# is the base value to generate random data.
random.seed(2000)

# این کد را چندین بار اجرا کنید و خروجی را بررسی کنید
# سپس خط بالا را کامنت کنید و چند بار برنامه را اجرا کنید
print(random.choice(["A","B"]))
print(random.choice(["A","B"]))
print(random.choice(["A","B"]))
print(random.choice(["A","B"]))

"""
Output always is:

B
A
B
B
"""