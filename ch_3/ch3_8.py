# numpy arrag [start:end[:step]]

import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"陣列元素如下 : {x}")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:2]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[-1]       = {x[-1]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::]       = {x[::]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")
