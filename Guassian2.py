import cv2
img = cv2.imread("C:/Users/OWNER/Desktop/sample3/Coker Treasure.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianBlurImage.jpg",gaussianBlurImg)
