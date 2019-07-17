import cv2
import numpy as np
image = cv2.imread('rectangle.png',0)
rows,cols = image.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(image,M,(cols,rows))
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()