import cv2
import imutils
img = cv2.imread("C:\\Users\\OWNER\\Desktop\\sample3\\sunflower.jpg")
resizeImg = imutils.resize(img, width = 20)
cv2.imwrite("resizedImg.jpg",resizeImg)
