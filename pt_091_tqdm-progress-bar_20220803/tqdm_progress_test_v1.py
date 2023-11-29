import time
import math
from tqdm import tqdm
from joblib import Parallel, delayed

"""
Professional Progress Bars in Python
https://www.youtube.com/watch?v=oJLaA7-i3nI
"""

results = []

# for loop
# for i in tqdm(range(18000)):
#     results.append(math.factorial(i))

# list comprehention
print("Progress bar WITHOUT Parallel(joblib)")
result = [math.factorial(x) for x in tqdm(range(8000))]

# using Parallel and delayed from joblib
print("\n" + "Progress bar with Parallel (should be 2x faster)")
result = Parallel(n_jobs=2)(delayed(math.factorial)(x) for x in tqdm(range(8000)))

print("\n" + "Progress bar with Parallel (usin all cores available)")
result = Parallel(n_jobs=-1)(delayed(math.factorial)(x) for x in tqdm(range(8000)))

print("")

