# 寫檔案
import cv2

cv2.namedWindow("MyPicture")
img = cv2.imread("jk.jpg")
cv2.imshow("Mypicture", img)

ret = cv2.imwrite("out1_7_1.tiff", img)
if ret:
    print("檔案儲存成功!")
else:
    print("檔案儲存失敗!")

ret = cv2.imwrite("out1_7_2.png", img)
if ret:
    print("檔案儲存成功!")
else:
    print("檔案儲存失敗!")

cv2.waitKey(3000)
cv2.destroyAllWindows()
