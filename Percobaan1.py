import cv2
import numpy as np

img = cv2.imread("ha.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gambar original", img)
cv2.imshow("gambar grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
