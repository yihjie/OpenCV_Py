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
---
# Scharr()
- 與 Sobel () 方式相同，但矩陣的權重不同
- x : [[ -3  0   3],
       [-10  0  10],
       [ -3  0   3]]

- y : [[-3 -10 -3],
       [ 0   0  0],
       [ 3  10  3]]
- 強調更微弱的影像邊緣，但可能讓整個影像邊緣顯得更複雜

---
# Laplacian()
- 法國 Pierre-Simon Laplace 發明
- 二階微分
- 一組 3x3 矩陣
- [[0  1  0],
   [1 -4  1],
   [0  1  0]]
- dst = cv2.Laplacian(src, ddepth, ksize, scale, delta, borderType)
  * ksize 一般設定為 3
- 建議先使用 cv2.GaussianBlur() 降低噪音

---
# Canny()
- 1986 澳洲 John F. Canny 開發
- 多級邊緣檢測演算法
- 邊緣檢測計算理論 ( Computational edge detection)
  * 好的檢測 : 盡可能標出影像的實際邊緣
  * 好的定位 : 標出的邊緣要與實際影像相符
  * 最小響應 : 邊緣只標出一次，雜訊不被標示為邊緣
- 執行步驟
1. 降低噪音 ( Noise Reduction )
2. 找尋影像的亮度梯度 ( Find Intensity Gradient of the Image )
3. 非最大值則抑制 ( Non-maximum Suppression )
4. 滯後閾值 ( Hysteresls Thresholding )
   1) if pixel gradient > maxVal --> Edge
   2) if pixel gradient < minVal --> Non-Edge
   3) if minVal < pixel < maxVal , pixel linked Edge --> Edge
- dst = cv2.Canny(image, threshold1, threshold2, edges, apertureSize = 3, L2gradient = False)
    * threshold1 : minVal
    * threshold2 : maxVal
    * L2gradient
      * True  : Edge_Gradient(G) = (G(x)^2 + G(y)^2)^(1/2)
      * False : Edge_Gradient(G) = Abs(G(x)) + Abs(G(y))