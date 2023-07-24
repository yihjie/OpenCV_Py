# 中文字
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def cv2_Chinese_Text(img, text, left, top, textColor, fontSize):
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype("C:\Windows\Fonts\mingliu.ttc", fontSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)

    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

img = cv2.imread('antarctic.jpg')
img = cv2_Chinese_Text(img, "我在南極", 220, 100, (0, 0, 255), 50)

cv2.imshow("中文字", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
