# 使用索引列印內容
import numpy as np

x = np.array([[1, 2, 3], [4, 5 ,6]])
print(x[0][2])
print(x[1][2])
print("-" * 70)
print(x[0, 2])
print(x[1, 2])
