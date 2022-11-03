import cv2

img = cv2.imread("cat.jpg")
r,col,color = img.shape
reshape_img = cv2.resize(img, dsize = (200,150))
cv2.imshow("image",reshape_img)
cv2.waitKey(0)
cv2.destroyAllWindows()