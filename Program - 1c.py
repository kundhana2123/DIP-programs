import cv2
img = cv2.imread("cat.jpg",0)
a,b = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img_b = np.concatenate((img, b), axis=1)
cv2.imshow('gray scale image and binary image', img_b)
cv2.waitKey(0)
cv2.destroyAllWindows()