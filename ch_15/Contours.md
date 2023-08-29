# 輪廓 ( contours)
- 分析影像中可能的形狀
- 影像內圖形或是一些外形的邊緣線條

---
# 找尋圖尋輪廓 cv2.findContours()
- contours, hierarchy = cv2.findContours(image, mode, method)
  - contours
    * 影像中所找到的所有輪廓
    * numpy.ndarry
      * 輪廓內的像素點座標
  - hierarchy
    * 輪廓間的層次關係
  - image
    * 必須是 8bit 的單通道影像(彩色 -> 灰階 -> 二值影像)
  - mode
    * RETR_EXTERNAL : 0 : 只檢測外部輪廓
    * RETR_LIST     : 1 : 檢測所有輪廓，但不建立層次關係
    * RETR_CCOMP    : 2 : 檢測所有輪廓，同時建立兩個層次關係
    * RETR_TREE     : 3 : 檢測所有輪廓，同時建立一個樹狀層次關係
  - method
    * CHAIN_APPROX_NONE     : 1 : 儲存所有輪廓點
    * CHAIN_APPROX_SIMPLE   : 2 : 只有保存輪廓頂點的座標, 只保存某個方向的兩個點 (最常用)
    * CHAIN_APPROX_TC89L1   : 3 : 使用 Teh-Chinl Chain 演算法
    * CHAIN_APPROX_TC89KCOS : 4 : 使用 Teh-Chinl Chain 演算法

---
# 繪製圖形的輪廓 cv2.drawContours()
- image = cv2.drawContours(src_image, contours, contourIdx, color, thickness, lineType, hierarchy, maxLevel, offset)
  - contourIdx : -1 表示繪製所有輪廓
  - color :　使用 BGR 格式
  - maxLevel : 0 表示繪製第 0 層， n 表示繪製 0 ~ n 層

---
# 應用
1. 原始圖形轉二值影像
   * cv2.cvtColor()  : 轉灰階
   * cv2.threshold() : 轉二值