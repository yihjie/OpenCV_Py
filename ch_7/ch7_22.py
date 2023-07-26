# 顯示所按的滑鼠事件名稱、滑鼠所在座標

import cv2
import numpy as np

def OnMouseAction(event, x ,y ,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:              # 按一下滑鼠左鍵
        msg_text = "按一下滑鼠左鍵"
    elif event == cv2.EVENT_RBUTTONDOWN:            # 按一下滑鼠右鍵
        msg_text = "按一下滑鼠右鍵"
    elif event == cv2.EVENT_MBUTTONDOWN:            # 按一下滑鼠中鍵
        msg_text = "按一下滑鼠中鍵"
    elif event == cv2.EVENT_MOUSEHWHEEL:            # 推動滑鼠滾輪
        msg_text = "推動滑鼠滾輪"
    elif flags == cv2.EVENT_FLAG_LBUTTON:           # 按住滑鼠左鍵拖曳
        msg_text = "按住滑鼠左鍵拖曳"
    elif flags == cv2.EVENT_FLAG_RBUTTON:           # 按住滑鼠右鍵拖曳
        msg_text = "按住滑鼠右鍵拖曳"
    elif flags == cv2.EVENT_FLAG_MBUTTON:           # 按住滑鼠中鍵拖曳
        msg_text = "按住滑鼠中鍵拖曳"
    elif event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
        msg_text = "滑鼠移動"
    else:
        msg_text = event
    print(f"在 x = {x}, y = {y} 執行 {msg_text}")

image = np.ones((200, 300, 3), np.uint8) * 255

cv2.namedWindow("OpenCV Mouse Event")
cv2.setMouseCallback("OpenCV Mouse Event", OnMouseAction)
cv2.imshow("OpenCV Mouse Event", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
