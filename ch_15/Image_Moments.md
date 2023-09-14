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
    * 零階 m00 (面積)
    * 一階 m10, m01 (求圓心) x = m10/m00 , y = m01/m00
    * 二階 m20, m11, m02
    * 三階 m30, m21, m12, m03
  * 中心矩
    * 二階 mu20, mu11, mu02
    * 三階 mu30, mu21, mu12, mu03
  * 歸一化中心矩
    * 二階 nu20, nu11, nu02
    * 三階 nu30, nu21, nu12, nu03
---
## 輪廓外型的匹配 - Hu 矩
Hu 矩 = 歸一化中心矩的線性組合
- 平移、縮放、旋轉時保持不變的特性
- hu = cv2.HuMoments(m) 回傳<font color='red'> 7 </font>個 Hu 矩
-  m = cv2.moments(array, binaryImage)

---
## 輪廓匹配
- retval = cv2.matchShapes(contour1, contour2, method, parameter)
  * retval    : 比較結果
  * contour1  : 輪廓 / 灰階影像
  * contour2  : 輪廓 / 灰階影像
  * method    : 比較方法
    * m(A) = sign(h(A)) * log(h(A))
    * m(B) = sing(h(B)) * log(h(B))
    
    * <font color='red'>常用</font> CONTOURS_MATCH_I1    : SUM(ABS(1/m(A) - 1/m(B))) from 1 ... 7 
    * CONTOURS_MATCH_I2    : SUM(ABS(m(A) - m(B))) from 1 ... 7
    * CONTOURS_MATCH_I3    : MAX(ABS(m(A) - m(B)) / ABS(m(A))) from 1 ... 7

---
## 輪廓外型匹配
1. 建立形狀場景距離
  - sd = cv2.createShapeContextDistanceExtractor()
  - retval = sd.compteDistance(contour1, contour2)
  - 相同輪廓的距離是 0 ，距離值越大，輪廓相差越大
  - 需要額外的 opencv 套件
    - pip install open-cv-contrib-python
2. Hausdorff 距離 ( 豪斯多夫距離)
  - max surface distance (MSD : 最大表面距離) 
  - h(A, B) = max(a in A)(min(b in B)(d(a, b)))
  - 理論參考說明 http://cgm.cs.mcgill.ca/~godfried/teaching/cg-projects/98/normand/main.html
  - hd = cv2.createHausdorffDistanceExtractor()
  - retval = hd.computeDistance(contour1, contour2)
