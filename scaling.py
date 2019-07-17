import cv2
image = cv2.imread('rectangle.png')
result = cv2.resultize(image,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
cv2.imshow("shapes",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
