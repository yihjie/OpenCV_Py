import cv2

src = cv2.imread('easy.jpg')
src_copy = src.copy()
# 1.
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 2.
ret , dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 3.
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 4.
dst = cv2.drawContours(src, contours, -1, (0, 0, 255), 5)

for c in contours:
    M = cv2.moments(c)
    Cx = int(M['m10'] / M['m00'])
    Cy = int(M['m01'] / M['m00'])
    cv2.circle(dst, (Cx, Cy), 5, (255, 255, 0), -1)
    str_text = '( ' + str(Cx) + ', ' + str(Cy) + ' )'
    cv2.putText(dst, str_text, (Cx - 20, Cy + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('Src', src_copy)
cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
