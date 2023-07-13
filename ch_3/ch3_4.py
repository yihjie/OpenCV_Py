# 建立內容是 0 的多維陣列
# 實務上，使用此方式來建立一張全黑影像 或 fill(255) 建立一張全白影像
import numpy as np

x1 = np.zeros(3)
print(x1)
print("-" * 70)

x2 = np.zeros((2, 3), dtype=np.uint8)
print(x2)
