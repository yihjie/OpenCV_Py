# Image moments - 影像矩 : 輪廓的特徵
- 輪廓的特徵
  * 質心
  * 面積
  * 周長
  * 邊界框
- 日常應用
  * 模式識別
  * 影像識別

---
## 矩特徵函數 : cv2.moments()
- 兩個輪廓是否相同 : 比較影像矩
- m = cv2.moments(array, binaryImage)
  * m : 影像矩、矩特徵
  * array : 計算矩特徵的輪廓點集合、灰階影像、二值影像
  * binaryImage : (Optional) True : array內非 0 == 1
- m 的資料內容
  * 空間矩
    * 零階矩 m00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
  * 中心矩
  * 歸一化中心矩
