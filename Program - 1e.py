import cv2
img = cv2.imread("cat.jpg")

#To rotate the image
resize_b = cv2.resize(img,dsize = (300,300))
image_90 = cv2.rotate(resize_b,cv2.cv2.ROTATE_90_CLOCKWISE)
image_180 = cv2.rotate(resize_b,cv2.ROTATE_180)
combine_image = np.concatenate((image_90,image_180), axis=1)
cv2.imshow("image",combine_image)
cv2.waitKey(0)
cv2.destroyAllWindows()