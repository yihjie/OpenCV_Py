import numpy as np

print("回傳單 3 個元素的陣列，值是 0(含)至 256(不含)的隨機數")
arr = np.random.randint(0, 256, size=3)
print(type(arr))
print(arr)
print("將陣列改為串列")
print(type(arr.tolist()))
print(arr.tolist())
