import numpy as np
import cv2
img = cv2.imread("cat.jpg")

#shape attribute gives the height, width and color of an image.
#Color is 3 because it is RGB image
height,width,color = img.shape

#blue image
a = np.zeros((height,width,color),np.uint8)
a[:,:,0] = img[:,:,0]
a = cv2.resize(a, dsize = (400,400))

#green image
b = np.zeros((height,width,color),np.uint8)
b[:,:,1] = img[:,:,1]
b = cv2.resize(b, dsize = (400,400))

#red image
c = np.zeros((height,width,color),np.uint8)
c[:,:,2] = img[:,:,2]
c = cv2.resize(c, dsize = (400,400))

#concatenates multiple images along specified axis
image_together = np.concatenate((a, b, c), axis=1)

cv2.imshow('Red, Green, Blue plane', image_together)
cv2.waitKey(0)
cv2.destroyAllWindows()