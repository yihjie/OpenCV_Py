# Image Pyramid (影像金字塔)
- 指一幅影像由不同解析度圖樣所組成的集合
- 常應用在 1. 影像壓縮 2. 機器視覺
- 原理
  - 同一幅影像，使用不斷向下採樣所產生的結果
    * 每採樣一次，影像尺寸會變小、解析度也變低
- 層次 ( level )
  - level 0 : 原始
  - level 1, level 2 , ...
- 向下採樣
  - 每增加一層，就刪除偶數列(row)、偶數行(column)
  - level 0 :　m x n
  - level 1 : (m/2) * (n/2)
  - level 2 : (m/4) * (n/4)
  - dst = cv2.pyrDown(src, dstsize, borderType)
    - dstsize : ((src.cols + 1) / 2, (src.rows + 1) / 2)
- 濾波器
  * 鄰域平均濾波器
  * 高斯濾波器 - 高斯金字塔(最常用)
- 向上採樣
  - 每增加一層，就讓影像的寬度、高度為原先的 2 倍
  - 最簡單的方式
    - 每一列下方增加一列、此列先暫時全補 0
    - 每一行右邊增加一行、此行先暫時全補 0
    - 使用插值處理，將 0 重新補值
  - dst = cv2.pyrUp(src, dstsize, borderType)
    - dstsize : ((src.cols * 2), (src.rows * 2))

---

# Laplacian Pyramid , LP (拉普拉斯金字塔)

