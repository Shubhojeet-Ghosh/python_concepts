import numpy as np
import time

# 10 million numbers
a = np.arange(10_000_000)
b = np.arange(10_000_000)

# NumPy vectorized (C-level loop)
start = time.time()
c = a + b
print("NumPy:", time.time() - start)

# Python loop
a_list = list(range(10_000_000))
b_list = list(range(10_000_000))
start = time.time()
c_list = [x + y for x, y in zip(a_list, b_list)]
print("Python:", time.time() - start)
