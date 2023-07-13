# 複製 array

import numpy as np

x1 = np.array([0, 1, 2, 3, 4, 5])
x2 = x1.copy()

print(x1)
print(x2)
print("-" * 70)
x2[0] = 9
print(x1)
print(x2)
