import cv2

src = cv2.imread('myheart.jpg')
src_copy = src.copy()
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# compare
match00 = cv2.matchShapes(contours[0], contours[0], cv2.CONTOURS_MATCH_I1,0)
match01 = cv2.matchShapes(contours[0], contours[1], cv2.CONTOURS_MATCH_I1,0)
match02 = cv2.matchShapes(contours[0], contours[2], cv2.CONTOURS_MATCH_I1,0)

for i in range(len(contours)):
    M = cv2.moments(contours[i])
    Cx = int(M['m10'] / M['m00'])
    Cy = int(M['m01'] / M['m00'])
    cv2.putText(src, str(i), (Cx - 3, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

print(f" 0 vs 0 = {match00}")
print(f" 0 vs 1 = {match01}")
print(f" 0 vs 2 = {match02}")

cv2.imshow('Result', src)

cv2.waitKey(0)
cv2.destroyAllWindows()
