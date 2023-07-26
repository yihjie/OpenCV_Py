# 列出所有 OpenCV 的事件(EVENT_)

import cv2

events = [i for i in dir(cv2) if "EVENT" in i]
for i in range(0, len(events)):
    print(f"{i+1} : {events[i]}")
