import time
import math
import random
from tqdm import tqdm, trange

"""
Professional Progress Bars in Python
https://www.youtube.com/watch?v=oJLaA7-i3nI
"""

with trange(1000) as t:
    for i in t:
        t.set_description(f"Iteration number {i+1}")
        sleeping_time = random.randint(1,100) / 100
        t.set_postfix(something=random.randint(0,100),
                      sleeping_time=sleeping_time)

        time.sleep(sleeping_time)

        if i % 100 == 0:
            for _ in trange(10):
                time.sleep(0.5)

