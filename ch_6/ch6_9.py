# 1. create 3 x 5 gray image array
# 2. using numpy.item() read values of the array
# 3. using itemset() to modify the [1,3] = 255

import numpy as np

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
image_copy = image.copy()

image.itemset((1, 3), 255)

print(f"修改前 image = \n{image_copy}")
print(f"修改後 image = \n{image}")
print("-" * 70)
print(f"修改前 image.item(1, 3) = {image_copy.item(1, 3)}")
print(f"修改後 image.item(1, 3) = {image.item(1, 3)}")
