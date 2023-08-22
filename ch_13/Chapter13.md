# 影像梯度 ( Image gradient )
- 影像強度與顏色方向的變化性
- 影像梯度大 == 影像邊緣 / 影像邊界
- 對於相機參數、拍攝亮度不敏感
---
# Sobel()
- 1968 年史丹福大學 Irwin Sobel , Gary Feldman 提出
- 高斯平滑 + 微分
- 包含兩組 3x3 矩陣
- x : [[-1  0  1],
       [-2  0  2],
       [-1  0  1]]

- y : [[-1 -2 -1],
       [ 0  0  0],
       [ 1  2  1]]
- dst = cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)
    * ddepth
      * -1 : 原始影像
      * cv2.CV_8U  : cv2.CV_16S, cv2.CV_32F, cv2.CV_64F
      * cv2.CV_16U : cv2.CV_32F
      * cv2.CV_16S : cv2.CV_64F
      * cv2.CV_32F : cv2.CV_32F, cv2.CV_64F
      * cv2.CV_64F : cv2.CV_64F
    * 建議目標影像深度必須設定比較大的深度，最後再取絕對值，映射為 cv2.CV_8U 