# 水平合併
import numpy as np

x1 = np.arange(4).reshape(2, 2)
x2 = np.arange(4, 8).reshape(2, 2)
x  = np.hstack((x1, x2))

print(f"x1 = \n{x1}")
print(f"x2 = \n{x2}")
print("-" * 70)
print(f"np.hstack((x1, x2)) = \n{x}")
