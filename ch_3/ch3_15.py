import numpy as np

x1 = [ 0,  1,  2,  3,  4]
x2 = [ 5,  6,  7,  8,  9]
x3 = [10, 11, 12, 13, 14]
x = np.array([x1, x2, x3])

print(f"x[:,:] -- 結果是 {np.ndim(x[:,:])} 維陣列")
print(x[:,:])
print("-" * 70)

print(f"x[2,:4] -- 結果是 {np.ndim(x[2,:4])} 維陣列")
print(x[2,:4])
print("-" * 70)

print(f"x[:2,:1] -- 結果是 {np.ndim(x[:2,:1])} 維陣列")
print(x[:2,:1])
print("-" * 70)

print(f"x[:,4:] -- 結果是 {np.ndim(x[:,4:])} 維陣列")
print(x[:,4:])
print("-" * 70)

print(f"x[:,4] -- 結果是 {np.ndim(x[:,4])} 維陣列")
print(x[:,4])
